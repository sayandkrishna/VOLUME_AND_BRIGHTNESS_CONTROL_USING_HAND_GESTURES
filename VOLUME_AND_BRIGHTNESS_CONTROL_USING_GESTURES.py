import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import screen_brightness_control as abc
from math import hypot

# Initialize MediaPipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2,
                       min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB for processing
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe hands
    results = hands.process(image_rgb)

    # List to store landmarks
    lmList = []

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, _ = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Calculate distance between thumb tip and index finger tip
            if len(lmList) >= 9:
                x1, y1 = lmList[4][1], lmList[4][2]
                x2, y2 = lmList[8][1], lmList[8][2]
                length = hypot(x2 - x1, y2 - y1)

                # Adjust brightness based on distance
                if lmList[0][1] < w/2: # left hand
                    brightness = np.interp(length, [15, 220], [0, 100])
                    abc.set_brightness(int(brightness))

                # Detect hand gesture
                if lmList[0][1] > w/2: # right hand
                    if lmList[4][2] > lmList[8][2]:
                        pyautogui.press('volumeup')
                    else:
                        pyautogui.press('volumedown')

    # Display the frame
    cv2.imshow('Hand Gesture', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()