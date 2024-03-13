from ursina import *
from math import radians
from entities import load_entities
from entities import load_corridor
import json
import sys


def resize_window():
    window.size = (window.size[0] + 1, window.size[1] + 1)
    time.sleep(0.1)
    window.size = (window.size[0] - 1, window.size[1] - 1)

def read_fromFile(filename):
  try:
    with open(filename, 'r') as file:
        data = json.load(file)
        left_pupil_location = data.get('left_pupil_location')
        left_relative = data.get('left_relative_pupil_position')
        right_pupil_location = data.get('right_pupil_location')
        right_relative = data.get('right_relative_pupil_position')

        if left_relative is None:
            left_relative = [-3, -2]
        if left_pupil_location is None:
            left_pupil_location = [270, 220]
        if right_pupil_location is None:
            right_pupil_location = [270, 220]
        if right_relative is None:
            right_relative = [0, -2]

        time.sleep(0.001)
        leftY = left_pupil_location[1]
        rightY = right_pupil_location[1]
        averageY = (leftY+rightY)/2

        leftX = left_relative[0]
        rightX = right_relative[0]
        averageX = (leftX + rightX)/2

        return averageX, averageY

  except json.JSONDecodeError:
        print(f"{filename} could not be read or is a corrupted file.")
        return [-1, 190]


class CarController(Entity):
    def __init__(self, car, **kwargs):
        super().__init__()

        self.max_x = 50  # X axis max
        self.min_x = -50  # X axis min
        self.max_z = 50  # Z axis max
        self.min_z = -50  # Z axis min

        self.car = car  # attach car and control
        self.can_move_forward = True
        self.collisionCounter = 0

        self.speed = 1.7  # car speed
        self.turn_speed = 5  # car spin
        self.camera = EditorCamera()
        self.camera.parent = car

        self.camera.rotation = (0, 0, 0)
        self.camera.position = (0, 0, 21.4)
        camera.fov = 85

        self.midPointCalibrate = read_fromFile('calibration_coord.json')
        self.closeButtonX = read_fromFile('close_button_cord.json')

        # text area for eye tracking coords
        self.collision_counter_text = Text(text='', position=(-0.1, 0.1), scale=2, color=color.yellow)
        self.pupil_location_text = Text(text='', position=(0, 0.5), scale=1)
        self.relative_pupil_position_text = Text(text='', position=(0, 0.45), scale=1)
        self.midPoint_text = Text(text='', position=(0, 0.4), scale=1)
        self.closeButtonX_text = Text(text='', position=(0, 0.35), scale=1)
        self.backButton_text = Text(text='', position=(0, 0.3), scale=1)
        self.collision_text = Text(text='Collision!', origin=(0, 0), background=True, scale=2, color=color.red)
        self.collision_text.enabled = False

        for key, value in kwargs.items():
            setattr(self, key, value)


    def update(self):
        pupil_posX, pupil_posY = read_fromFile('eye_tracking_data.json')
        hit_info = self.car.intersects()

        if hit_info.hit:
            self.can_move_forward = False
            if not self.collision_text.enabled:
                self.collision_text.enabled = True
                self.collisionCounter += 1


        else:# if no collision, release the vehicle
            self.can_move_forward = True
            if self.collision_text.enabled:
                self.collision_text.enabled = False

        # update text area
        self.pupil_location_text.text = f'Pupil Location: {pupil_posY}'
        self.relative_pupil_position_text.text = f'Relative Pupil Position: {pupil_posX}'
        self.midPoint_text.text = f'Mid point is: {self.midPointCalibrate}'
        self.closeButtonX_text.text = f'close point is: {self.closeButtonX}'


        if pupil_posX and pupil_posY:
            distance_from_center = abs(pupil_posX - self.midPointCalibrate[0])
            # spin scale
            turn_sense = distance_from_center / abs(self.closeButtonX[0]/7)
            if self.closeButtonX[0]-2 > pupil_posX and self.closeButtonX[1] > pupil_posY:
                self.collision_counter_text.text = f'Collision Counter: {self.collisionCounter}'
                invoke(self.end_game, delay=1)
            if pupil_posY < self.midPointCalibrate[1] and self.can_move_forward:
                self.move_forward()

            if pupil_posX < self.midPointCalibrate[0]-2:
                self.car.rotation_y += self.turn_speed * turn_sense * time.dt
            elif pupil_posX > self.midPointCalibrate[0]+2:
                self.car.rotation_y -= self.turn_speed * turn_sense * time.dt

    def move_forward(self):
        forward = sin(radians(self.car.rotation_y))
        backward = cos(radians(self.car.rotation_y))
        self.car.x += self.speed * forward * time.dt
        self.car.z += self.speed * backward * time.dt

    def end_game(self):
        sys.exit()

def save_map_flag(value):
    with open('map_flag.json', 'w') as file:
        json.dump({'mapFlag': value}, file)

def load_map_flag():
    try:
        with open('map_flag.json', 'r') as file:
            data = json.load(file)
            return data.get('mapFlag', True)  # If the file does not exist, it returns True by default.
    except FileNotFoundError:
        return True  # If the file is not found, it returns True by default.

def toggle_map_flag():
    current_flag = load_map_flag()
    save_map_flag(not current_flag)

mapFlag = load_map_flag()
app = Ursina(fullscreen=True)
if mapFlag == True:
    window.color = color.rgb(135, 206, 235)
    entities = load_entities()
    car = entities['car']
    car_controller = CarController(car)


elif mapFlag == False:
    window.color = color.rgb(255, 165, 0)  # orange color
    walls = load_corridor()
    car = walls['car']
    car_controller = CarController(car)


def update():
    car_controller.update()

invoke(resize_window, delay=0.1)
#toggle_map_flag()
app.run()
