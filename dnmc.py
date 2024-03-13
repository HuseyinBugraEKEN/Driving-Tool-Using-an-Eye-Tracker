import dlib
import cv2
import time
import json
import Cocoa
import Quartz

detector = dlib.get_frontal_face_detector()
path = '/Users/bugrabey/Desktop/Driving_Tool_Using_an_Eye_Tracker/shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(path)

def set_window_always_on_top(window_title):
    app = Cocoa.NSApplication.sharedApplication()
    windows = app.windows()
    for window in windows:
        title = window.title()
        if title == window_title:
            window.setLevel_(Quartz.kCGFloatingWindowLevel)
            break

def write_to_file(data1, data2, filename):
    if data1 is None:
        data1 = {
            "left_pupil_location": [275, 220],
            "left_relative_pupil_position": [-3, -2]
        }
    if data2 is None:
        data2 = {
            "right_pupil_location": [275, 220],
            "right_relative_pupil_position": [0, -2]
        }

    combined_data = {**data1, **data2}
    with open(filename, "w") as file:
        json.dump(combined_data, file)


def is_close(y0, y1):
    if abs(y0 - y1) < 9:
        return True
    return False


def get_center(gray_img):
    moments = cv2.moments(gray_img, False)
    try:
        return int(moments['m10'] / moments['m00']), int(moments['m01'] / moments['m00'])
    except:
        return None


def p(img, parts, eye):
    if eye[0]:
        cv2.circle(img, eye[0], 3, (255, 255, 0), -1)
    if eye[1]:
        cv2.circle(img, eye[1], 3, (255, 255, 0), -1)
    for i in parts:
        cv2.circle(img, (i.x, i.y), 3, (255, 0, 0), -1)

    cv2.imshow("me", img)


def get_eye_parts(parts, left=True):
    if left:
        eye_parts = [
            parts[36],
            min(parts[37], parts[38], key=lambda x: x.y),
            max(parts[40], parts[41], key=lambda x: x.y),
            parts[39],
        ]
    else:
        eye_parts = [
            parts[42],
            min(parts[43], parts[44], key=lambda x: x.y),
            max(parts[46], parts[47], key=lambda x: x.y),
            parts[45],
        ]
    return eye_parts


def get_eye_image(img, parts, left=True):
    if left:
        eyes = get_eye_parts(parts, True)
    else:
        eyes = get_eye_parts(parts, False)
    org_x = eyes[0].x
    org_y = eyes[1].y

    if is_close(org_y, eyes[2].y):
        return None
    eye = img[org_y:eyes[2].y, org_x:eyes[-1].x]

    if left:
        #cv2.imshow("left",eye)
        cv2.moveWindow('left', 50, 200)
    else:
        #cv2.imshow("right",eye)
        cv2.moveWindow('right', 350, 200)
    return eye


def get_eye_center(img, parts, left=True):
    if left:
        eyes = get_eye_parts(parts, True)
    else:
        eyes = get_eye_parts(parts, False)

    x_center = int(eyes[0].x + (eyes[-1].x - eyes[0].x) / 2)
    y_center = int(eyes[1].y + (eyes[2].y - eyes[1].y) / 2)

    cv2.circle(img, (x_center, y_center), 3, (255, 255, 0), -1)
    return x_center, y_center


def get_pupil_location(img, parts, left=True):
    if left:
        eyes = get_eye_parts(parts, True)
    else:
        eyes = get_eye_parts(parts, False)
    org_x = eyes[0].x
    org_y = eyes[1].y
    if is_close(org_y, eyes[2].y):
        return None
    eye = img[org_y:eyes[2].y, org_x:eyes[-1].x]
    _, threshold_eye = cv2.threshold(cv2.cvtColor(eye, cv2.COLOR_RGB2GRAY), 45, 255, cv2.THRESH_BINARY_INV)

    if left:
        #cv2.imshow("left_threshold",eye)
        cv2.moveWindow('left_threshold', 50, 300)
    else:
        #cv2.imshow("right_threshold",eye)
        cv2.moveWindow('right_threshold', 350, 300)

    center = get_center(threshold_eye)
    if center:
        cv2.circle(img, (center[0] + org_x, center[1] + org_y), 3, (255, 0, 0), -1)
        return center[0] + org_x, center[1] + org_y
    return center


def calculate_relative_pupil_position(img, eye_center, pupil_locate, left=True):
    if not eye_center:
        return
    if not pupil_locate:
        return

    relative_pupil_x = pupil_locate[0] - eye_center[0]
    relative_pupil_y = pupil_locate[1] - eye_center[1]
    if left:
        cv2.putText(img,
                    "eye center x=" + str(eye_center[0]) + " y=" + str(eye_center[1]),
                    org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.8,
                    color=(0, 255, 0),
                    thickness=2,
                    lineType=cv2.LINE_4)
        cv2.putText(img,
                    "pupil Locate x=" + str(pupil_locate[0]) + " y=" + str(pupil_locate[1]),
                    org=(50, 100),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.8,
                    color=(0, 255, 0),
                    thickness=2,
                    lineType=cv2.LINE_4)
        cv2.putText(img,
                    "relative pupil x=" + str(relative_pupil_x) + " y=" + str(relative_pupil_y),
                    org=(50, 150),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.8,
                    color=(0, 255, 0),
                    thickness=2,
                    lineType=cv2.LINE_4)
    return relative_pupil_x, relative_pupil_y

Wvalue = 720
Hvalue = 480
prev_frame_time = time.time()
cap = cv2.VideoCapture(0)
time.sleep(2)
# Set a lower resolution for the camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, Wvalue)#720-1280
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, Hvalue)#480-720

cv2.namedWindow("me", cv2.WINDOW_NORMAL)
ret, frame = cap.read()
cv2.imshow("me", frame)
cv2.resizeWindow("me", 370, 280)  # 500,280
cv2.moveWindow("me", 0, 0)

is_calibrated = False
window_open = True

while ret:
    ret, frame = cap.read()
    # Check if a frame was successfully captured
    if not ret:
        print("Failed to capture frame")
        time.sleep(0.1)
        continue

    dets = detector(frame[:, :, ::-1])
    if len(dets) > 0:
        parts = predictor(frame, dets[0]).parts()
    else:
        parts = None

    if parts:
        left_eye_image = get_eye_image(frame, parts, True)
        right_eye_image = get_eye_image(frame, parts, False)
        left_eye_center = get_eye_center(frame, parts, True)
        right_eye_center = get_eye_center(frame, parts, False)
        left_pupil_location = get_pupil_location(frame, parts, True)
        right_pupil_location = get_pupil_location(frame, parts, False)
        left_relative_pupil_position = calculate_relative_pupil_position(frame, left_eye_center, left_pupil_location, True)
        right_relative_pupil_position = calculate_relative_pupil_position(frame, right_eye_center, right_pupil_location, False)

        left_data = {
            "left_pupil_location": left_pupil_location,
            "left_relative_pupil_position": left_relative_pupil_position
        }
        right_data = {
            "right_pupil_location": right_pupil_location,
            "right_relative_pupil_position": right_relative_pupil_position
        }

        write_to_file(left_data, right_data, "eye_tracking_data.json")
        time.sleep(0.01)

        key = cv2.waitKey(1)
        if key == ord(' '):
            write_to_file(left_data, right_data, "calibration_coord.json")
            is_calibrated = True
        elif key == ord('q'):
            write_to_file(left_data, right_data, "close_button_cord.json")
        elif key == 27:
            break
        time.sleep(0.01)

        height, width = frame.shape[:2]
        start_point_vertical = (width // 2, 0)
        end_point_vertical = (width // 2, height)
        start_point_horizontal = (0, height // 3)
        end_point_horizontal = (width, height // 3)
        cv2.line(frame, start_point_vertical, end_point_vertical, (255, 0, 0), 2)
        cv2.line(frame, start_point_horizontal, end_point_horizontal, (255, 0, 0), 2)
        if not is_calibrated:
            cv2.putText(frame, "Look at the upper right corner and press 'q'", (40, 375), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)
            cv2.putText(frame, "Look at the midpoint and press 'Space'", (40, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)
            cv2.putText(frame, "15 second for calibration", (40, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)

    new_frame_time = time.time()
    # Calculating the fps
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    fps_text = f"FPS: {fps:.2f}"
    cv2.putText(frame, fps_text, (450, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 255, 0), 2, cv2.LINE_AA)
    if window_open:
        cv2.imshow("me", frame)
        set_window_always_on_top("me")


cap.release()
cv2.destroyAllWindows()