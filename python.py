import cv2
import mediapipe as mp
import serial
import time

# Initializing serial communication with Arduino
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
time.sleep(2)  # Wait for the serial connection to initialize

# Initializing Mediapipe with optimized settings
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Function to detect individual fingers (1 for up, 0 for down)
def detect_fingers(hand_landmarks):
    finger_tips = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky
    thumb_tip = 4
    finger_states = [0] * 5  # Thumb, Index, Middle, Ring, Pinky

    # Check thumb
    if hand_landmarks.landmark[thumb_tip].x < hand_landmarks.landmark[thumb_tip - 1].x:
        finger_states[0] = 1  # Thumb is up

    # Check other fingers
    for idx, tip in enumerate(finger_tips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            finger_states[idx + 1] = 1  # Other fingers are up

    return finger_states

# Start capturing video
cap = cv2.VideoCapture(0)
last_fingers_state = None  # Store the previous state to reduce serial communication

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Process the image for hand tracking
    image = cv2.flip(image, 1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_image)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingers_state = detect_fingers(hand_landmarks)

            # Send data only if the finger state has changed
            if fingers_state != last_fingers_state:
                arduino.write(bytes(fingers_state))  # Send list of fingers as bytes
                print(f"Fingers State: {fingers_state}")
                last_fingers_state = fingers_state  # Update last known state

    # Display the output
    cv2.imshow('Hand Tracking', image)
    if cv2.waitKey(5) & 0xFF == 27:  # Exit on pressing the ESC key
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
arduino.close()
