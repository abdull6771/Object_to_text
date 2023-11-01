import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
my_config = r"--psm 11 --oem 3"
img = Image.open('aa.jpg')
text = tess.image_to_string(img,config=my_config)

print(text)
