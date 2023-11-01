import cv2
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread("plate_number.jpg")

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(tess.pytesseract.image_to_string(image=img))