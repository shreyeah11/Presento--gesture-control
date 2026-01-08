import math
import time

def classify_gesture(landmarks):
    if not landmarks or len(landmarks) < 21:
        return None

    wrist = landmarks[0]
    thumb = landmarks[4]
    index = landmarks[8]
    middle = landmarks[12]
    ring = landmarks[16]
    pinky = landmarks[20]
    
    # Tolerance value (in pixels)
    tol = 10
    
    # 1. Open Palm: All fingertips significantly above wrist (y-value smaller than wrist by at least tol)
    if (index[1] < wrist[1] - tol and middle[1] < wrist[1] - tol and
        ring[1] < wrist[1] - tol and pinky[1] < wrist[1] - tol):
        return "open_hand"
    
    # 2. Closed Fist: All fingertips significantly below wrist (y-value greater than wrist by tol)
    if (index[1] > wrist[1] + tol and middle[1] > wrist[1] + tol and
        ring[1] > wrist[1] + tol and pinky[1] > wrist[1] + tol):
        return "closed_fist"
    
    # 3. Thumb Gestures: Calculate the angle of the thumb relative to the wrist.
    # Note: In image coordinates, y increases downward.
    angle_thumb = math.degrees(math.atan2(thumb[1] - wrist[1], thumb[0] - wrist[0]))
    # For thumbs up: angle around -90 degrees (vertical upward)
    if -110 < angle_thumb < -70:
        return "thumbs_up"
    # For thumbs down: angle around 90 degrees (vertical downward)
    if 70 < angle_thumb < 110:
        return "thumbs_down"
    # For thumb pointing right: near 0 degrees (horizontal right)
    if -30 < angle_thumb < 30:
        return "thumb_right"
    # For thumb pointing left: near 180 or -180 degrees (horizontal left)
    if abs(angle_thumb) > 150:
        return "thumb_left"
    
    return None

def detect_swipe(landmarks, prev_wrist_x, threshold=100):
    if landmarks is None or prev_wrist_x is None:
        return None
    current_wrist_x = landmarks[0][0]
    diff = current_wrist_x - prev_wrist_x
    if diff > threshold:
        return "swipe_right"
    elif diff < -threshold:
        return "swipe_left"
    return None

def detect_dynamic_swipe(landmarks, prev_wrist_x, prev_timestamp, speed_threshold=400):
    if landmarks is None or prev_wrist_x is None or prev_timestamp is None:
        return None
    current_wrist_x = landmarks[0][0]
    current_time = time.time()
    delta_x = current_wrist_x - prev_wrist_x
    delta_time = current_time - prev_timestamp
    if delta_time <= 0:
        return None
    speed = abs(delta_x) / delta_time  # pixels per second
    if speed > speed_threshold:
        if delta_x > 0:
            return "swipe_right"
        else:
            return "swipe_left"
    return None
