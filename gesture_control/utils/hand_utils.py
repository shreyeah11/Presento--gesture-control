def extract_hand_landmarks(hand_landmarks, shape):
    height, width, _ = shape
    landmarks = []
    for lm in hand_landmarks.landmark:
        landmarks.append((int(lm.x * width), int(lm.y * height)))
    return landmarks
