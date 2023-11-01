import cv2
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from pytesseract import Output
my_config = r"--psm 9 --oem 3"
img = cv2.imread("image2.jpg")

hg,wg,_ = img.shape

boxes = tess.pytesseract.image_to_boxes(image=img,config=my_config)
text = tess.image_to_string(img,config=my_config)
data = tess.image_to_data(image=img,config=my_config,output_type=Output.DICT)

print(data["text"])

amount_of_boxes = len(data["text"])
for i in range(amount_of_boxes):
    if float(data["conf"][i]) > 90:
        (x,y,wg,hg) = (data["left"][i],data["top"][i],data["width"][i],data["height"][i])
        img = cv2.rectangle(img,(x,y),(x+wg,y+hg),(0,255,0),2)
        img = cv2.putText(img,data["text"][i],(x,y+hg+20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2,cv2.LINE_AA)



cv2.imshow("img",img)
cv2.waitKey(0)