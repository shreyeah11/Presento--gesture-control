import cv2
import mediapipe as mp
from utils.hand_utils import extract_hand_landmarks
from utils.geometry import classify_gesture, detect_swipe, detect_dynamic_swipe
from utils.draw_utils import draw_hand_annotations
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

prev_wrist_x = None
prev_timestamp = None

def detect_gesture(frame):
    global prev_wrist_x, prev_timestamp
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        landmarks = extract_hand_landmarks(hand_landmarks, frame.shape)
        draw_hand_annotations(frame, hand_landmarks)
        
        # First, check for dynamic (swipe) gestures:
        swipe = detect_swipe(landmarks, prev_wrist_x, threshold=40)
        # For fast swipe detection, compute time difference:
        current_time = time.time()
        dynamic_swipe = detect_dynamic_swipe(landmarks, prev_wrist_x, prev_timestamp, speed_threshold=200)
        
        # Update previous values:
        prev_wrist_x = landmarks[0][0]
        prev_timestamp = current_time
        
        if dynamic_swipe:
            return dynamic_swipe, landmarks
        if swipe:
            return swipe, landmarks
        
        # Otherwise, return static gestures:
        gesture_static = classify_gesture(landmarks)
        return gesture_static, landmarks
    else:
        prev_wrist_x = None
        prev_timestamp = None
        return None, None
