from ursina import *
import subprocess
import time
import json
import atexit
import threading

dnmc_started = False
dnmc_process = None
game_started = False
game_process = None
compare_data_flag = False
info_screen_active = False

def calibration_data(filename):
  try:
    with open(filename, 'r') as file:
        data = json.load(file)
        left_pupil_location = data.get('left_pupil_location')
        left_relative_position = data.get('left_relative_pupil_position')
        right_pupil_location = data.get('right_pupil_location')
        right_relative_position = data.get('right_relative_pupil_position')
        if left_relative_position is None:
            left_relative_position = [-3, -2]
        if left_pupil_location is None:
            left_pupil_location = [270, 220]
        if right_pupil_location is None:
            right_pupil_location = [270, 220]
        if right_relative_position is None:
            right_relative_position = [0, -2]

        leftY = left_pupil_location[1]
        rightY = right_pupil_location[1]
        averageY = (leftY + rightY) / 2

        leftX = left_relative_position[0]
        rightX = right_relative_position[0]
        averageX = (leftX + rightX) / 2
        return averageX, averageY

  except json.JSONDecodeError:
        print(f"{filename} could not be read or is a corrupted file.")
        return [-1, 190]


def compare_data(start_button, settings_button, hover_duration=3):
    global game_started
    pupilX, pupilY = calibration_data('eye_tracking_data.json')
    calibratedX, calibratedY = calibration_data('calibration_coord.json')


    if pupilX and pupilY:


        if calibratedY > pupilY and calibratedX+5 > pupilX > calibratedX-5:
            start_button.gaze_time += time.dt
            settings_button.gaze_time = 0
            print("for start:", f"{hover_duration-start_button.gaze_time:.1f}", "second left")
            if start_button.gaze_time >= hover_duration and not game_started:
                start_button.on_click()
                start_button.gaze_time = 0

        elif calibratedY+2 < pupilY and calibratedX+5 > pupilX > calibratedX-5:
            settings_button.gaze_time += time.dt
            start_button.gaze_time = 0
            if settings_button.gaze_time >= hover_duration:
                settings_button.on_click()
                settings_button.gaze_time = 0


def resize_window():
    window.size = (window.size[0] + 1, window.size[1] + 1)
    time.sleep(0.1)
    window.size = (window.size[0] - 1, window.size[1] - 1)


def start_dnmc():
    global dnmc_started, dnmc_process
    if not dnmc_started:
        dnmc_process = subprocess.Popen(['python3', 'dnmc.py'])
        dnmc_started = True
def stop_dnmc():
    global dnmc_process
    if dnmc_process:
        dnmc_process.terminate()


def start_game():
    global game_started, game_process
    if not game_started:
        print("Simulation is starting")
        game_process = subprocess.Popen(['python3', 'pannda.py'])
        game_started = True
        threading.Thread(target=monitor_game_process).start()

def monitor_game_process():
    global game_started, game_process
    game_process.wait()  # Wait for the game process to terminate
    game_started = False
    reset_system()

def settings_info_screen():
    global info_screen_active
    info_screen_active = True
    info_text1 = Text(text="Look at the upper right corner\nand press 'q'", scale=1.2, color=color.red, position=(0.37, 0.46))
    info_text3 = Text(text="Look at the middle of the screen\nand press 'space'", scale=1.2, color=color.red, position=(-0.23, 0))
    info_image = Entity(model='quad', texture='user-position', scale=(4, 3.5), position=(-5, 0))

    def close_info_screen():
        global info_screen_active
        info_text1.enabled = False
        info_text3.enabled = False
        info_image.enabled = False
        info_screen_active = False
        reset_system()
    invoke(close_info_screen, delay=7)


def reset_system():
    global compare_data_flag
    # Turn on/off camera
    compare_data_flag = False
    set_compare_data_flag()

def settings():
    print("Settings....")
    settings_info_screen()


def arayuz():
    start_button = Button(text="Start", on_click=start_game)
    start_button.scale_y = 0.35
    start_button.scale_x = 0.5
    start_button.x = 0
    start_button.y = 0.25
    start_button.gaze_time = 0

    settings_button = Button(text="Settings", on_click=settings)
    settings_button.scale_y = 0.35
    settings_button.scale_x = 0.5
    settings_button.x = 0
    settings_button.y = -0.25
    settings_button.gaze_time = 0

    return start_button, settings_button


atexit.register(stop_dnmc)
app = Ursina(borderless=True, size=(1440, 1000))
start_button, settings_button = arayuz()
pupilX, pupilY = calibration_data('eye_tracking_data.json')


def input(key):
    global compare_data_flag
    if key == 'r':
        compare_data_flag = True


def set_compare_data_flag():
    global compare_data_flag
    compare_data_flag = True
timer = threading.Timer(15, set_compare_data_flag)
timer.start()


def update():

    global dnmc_started, compare_data_flag, game_started
    if not dnmc_started:
        start_dnmc()
    if dnmc_started and compare_data_flag and not game_started and not info_screen_active:
        compare_data(start_button, settings_button)
    #invoke(resize_window)
    if game_started:
        compare_data_flag = False

app.run()