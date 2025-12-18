import torch
from ultralytics import YOLO
import cv2

# Load YOLOv11 Model
model = YOLO("models/yolov11.pt")  # Ensure model file is in models/ folder

def detect_number_plate(image):
    results = model(image, conf=0.6)  # Increase confidence threshold

    
    for result in results:
        for box in result.boxes.xyxy:
            x1, y1, x2, y2 = map(int, box[:4])  # Get bounding box
            plate_image = image[y1:y2, x1:x2]
            return plate_image, (x1, y1, x2, y2)
    
    return None, None
