import torch
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
from PIL import Image
import pytesseract
import subprocess
import re
import query_db
import send_data


database = r"/home/youhaveme/yoloCar/sns-processing/cars_database.db"

model= torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    
    # Make detections 
    isExist = os.path.exists('runs/detect/exp3')
    results = model(frame)
    detect = str(results)
    extract=detect[detect.index("40")+2:detect.index("Speed")]
    finalExtract = ''.join(letter for letter in extract if letter.isalnum())
    print(finalExtract)
    
    cv2.imshow('YOLO', np.squeeze(results.render()))
    if(finalExtract=="nodetections"):
        continue
    if(finalExtract=="1plate" and isExist==False):
        crops = results.crop()
    if(isExist):
        raw_number = pytesseract.image_to_string(Image.open('runs/detect/exp2/crops/plate/image0.jpg'))
        car_number = ''.join(letter for letter in raw_number if letter.isalnum())
        currentDetection = car_number
        print("Car number:", car_number)
        conn = query_db.create_connection(database)
        data = query_db.select_all_tasks(conn)

        for rows in data:
            if rows[1] == car_number:
                send_data.send_update(car_number)
                send_data.send_update_to_app(car_number)
                send_data.update_tracking_details(car_number)
        subprocess.run(["rm -r /home/youhaveme/yoloCar/runs/detect"], shell=True)
        finalDetection=car_number
    else:
        continue

    if (cv2.waitKey(10) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()



