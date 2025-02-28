import cv2
import pandas as pd
import numpy as np
import csv 
import time
import mediapipe as mp
# Gesture Name 

gesture_name = input("Please Enter the Gesture Name")

file_path = f"data/raw/{gesture_name}.csv"

file = open(file_path , "w" , newline="")
writer = csv.writer(file)
print(f"Collecting the Data for the {gesture_name}")
time.sleep(5)
mp_hand = mp.solutions.hands
mp_drawing_utils = mp.solutions.drawing_utils
hands = mp_hand.Hands(min_detection_confidence = 0.7, min_tracking_confidence=0.7)

cam = cv2.VideoCapture(0)

while cam.isOpened():
    ret , frame = cam.read()
    if not ret:
        break




