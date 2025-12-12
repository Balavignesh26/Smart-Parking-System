from ultralytics import YOLO

# Load YOLOv11n model (this will automatically download it)
model = YOLO('yolov11n.pt')

print("Model downloaded successfully!")
