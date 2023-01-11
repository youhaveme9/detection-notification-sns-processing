# imports
import os
import re
import cv2
import torch
import subprocess
import pytesseract
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import query_db
import send_data


# stolen car local cached database
database = r"/home/youhaveme/yoloCar/sns-processing/cars_database.db"

# loading custom trained model
try:
    model = torch.hub.load('ultralytics/yolov5', 'custom',
                       path='model/best.pt', force_reload=True)
except Exception as e:
    print(e)

    
def detect_license_number(path):
    # detecting license plate number 
    raw_number = pytesseract.image_to_string(
            Image.open('runs/detect/exp2/crops/plate/image0.jpg'))
    car_number = ''.join(letter for letter in raw_number if letter.isalnum())
    currentDetection = car_number
    print("Car number:", car_number)
    conn = query_db.create_connection(database)
    data = query_db.select_all_tasks(conn)

    # sending notification
    for rows in data:
        if rows[1] == car_number:
            try:
                send_data.send_update(car_number)
                send_data.send_update_to_app(car_number)
                send_data.update_tracking_details(car_number)
            except Exception as e:
                print(e)
                break
        subprocess.run(
            ["rm -r /home/youhaveme/yoloCar/runs/detect"], shell=True)

def main():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        isExist = os.path.exists('runs/detect/exp3')
        # Extracting text - detecting or not
        results = model(frame)
        detect = str(results)
        extract = detect[detect.index("40")+2:detect.index("Speed")]
        finalExtract = ''.join(letter for letter in extract if letter.isalnum())
        print(finalExtract)

        cv2.imshow('License Plate Detection', np.squeeze(results.render()))
        if (finalExtract == "nodetections"):
            continue
        if (finalExtract == "1plate" and isExist == False):
            crops = results.crop()
        if (isExist):
            detect_license_number(path="runs/detect/exp2/crops/plate/image0.jpg")
        else:
            continue

        if (cv2.waitKey(10) & 0xFF == ord('q')):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
