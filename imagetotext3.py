import cv2
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

my_config = r"--psm 8 --oem 3"
img = cv2.imread("image2.jpg")

hg,wg,_ = img.shape

boxes = tess.pytesseract.image_to_boxes(image=img,config=my_config)
text = tess.image_to_string(img,config=my_config)

print(text)
file = open('read.txt', 'w') 
file.write(text) 
file.close()
for box in boxes.splitlines():
    box = box.split(" ")
    img = cv2.rectangle(img,(int(box[1]),hg- int(box[2])), (int(box[3]),hg-int(box[4])),(0,255,0),1)

cv2.imshow("img",img)
cv2.waitKey(0)