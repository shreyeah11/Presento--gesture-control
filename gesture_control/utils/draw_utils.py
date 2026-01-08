import cv2
import mediapipe as mp

mp_draw = mp.solutions.drawing_utils

def draw_hand_annotations(frame, hand_landmarks):
    mp_draw.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
