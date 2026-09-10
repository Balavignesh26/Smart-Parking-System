import cv2
from detect_plate import detect_number_plate
from ocr import extract_text
from parking_management import manage_parking

cap = cv2.VideoCapture(0)  # Open camera

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Detect Number Plate
    plate_image, plate_bbox = detect_number_plate(frame)

    if plate_image is not None:
        plate_text = extract_text(plate_image)
        print(f"Detected Plate: {plate_text}")

        # Manage Parking
        manage_parking(plate_text)

    cv2.imshow("Live Feed", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
