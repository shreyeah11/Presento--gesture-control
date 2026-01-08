import cv2
import time
from gesture_recognition import detect_gesture
from command_executor import execute_command
from config import GESTURE_COMMAND_MAPPING
from utils.timer_utils import Timer

timer = Timer()
DEBOUNCE_DELAY = 0.5  # Reduced delay for responsiveness

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gesture, landmarks = detect_gesture(frame)

    if gesture and timer.should_trigger(DEBOUNCE_DELAY):
        command = GESTURE_COMMAND_MAPPING.get(gesture)
        if command:
            print(f"Detected gesture: {gesture} -> Executing command: {command}")
            execute_command(command)

    cv2.imshow("Presento - Hand Gesture Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
