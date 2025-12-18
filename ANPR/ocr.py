import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\jayan\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
def extract_text(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return pytesseract.image_to_string(gray, config="--psm 7").strip()


def preprocess_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    blur = cv2.GaussianBlur(gray, (5,5), 0)  # Reduce noise
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)  # Binarize
    return thresh

roi = preprocess_image(plate_region)
plate_text = pytesseract.image_to_string(roi, config='--psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
