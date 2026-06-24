import cv2
import mediapipe as mp
import math
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VIDEO_PATH = os.path.join(BASE_DIR, "scubacat.mp4")
CAMERA_INDEX = 0

CAMERA_WINDOW = "Main Camera"
MEME_WINDOW = "Meme Video"


mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8
)


cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Could not open webcam.")
    exit()

meme_cap = None
video_on = False


def points_close(p1, p2, threshhold=0.25):
    distance = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
    return distance < threshhold


def is_fist(lm):
    fingertips = [8, 12, 16, 20]
    wrist = lm[0]

    closed_fingers = []

    for tip in fingertips:
        finger_closed = points_close(lm[tip], wrist)
        closed_fingers.append(finger_closed)

    return all(closed_fingers)


def is_open_palm(lm):
    tip_and_joint_pairs = [
        (8, 6),
        (12, 10),
        (16, 14),
        (20, 18)
    ]

    open_fingers = []

    for tip, joint in tip_and_joint_pairs:
        finger_open = lm[tip].y < lm[joint].y
        open_fingers.append(finger_open)

    return all(open_fingers)


def start_meme():
    global meme_cap, video_on

    if not os.path.exists(VIDEO_PATH):
        print(f"Could not find {VIDEO_PATH}")
        return

    meme_cap = cv2.VideoCapture(VIDEO_PATH)

    if meme_cap.isOpened():
        video_on = True
        print("Fist detected.")


def stop_meme():
    global meme_cap, video_on

    video_on = False

    if meme_cap is not None:
        meme_cap.release()
        meme_cap = None

    try:
        cv2.destroyWindow(MEME_WINDOW)
    except cv2.error:
        pass


def show_meme():
    global meme_cap

    if meme_cap is None:
        return

    ret, meme_frame = meme_cap.read()

    if not ret:
        meme_cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, meme_frame = meme_cap.read()

    if not ret:
        return

    meme_frame = cv2.resize(meme_frame, (400, 400))
    cv2.imshow(MEME_WINDOW, meme_frame)


while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not read from webcam")
        break

    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb_frame)

    fist_detected = False
    palm_detected = False

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            lm = hand_landmarks.landmark

            if is_fist(lm):
                fist_detected = True

            elif is_open_palm(lm):
                palm_detected = True

        if fist_detected and not video_on:
            start_meme()

        elif palm_detected and video_on:
            stop_meme()

    if video_on:
        show_meme()

    cv2.imshow(CAMERA_WINDOW, frame)

    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break

cap.release()

if meme_cap is not None:
    meme_cap.release()

cv2.destroyAllWindows()
