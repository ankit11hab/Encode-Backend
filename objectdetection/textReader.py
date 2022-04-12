import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread('ocr2.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
th,threshed = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
text = pytesseract.image_to_string(threshed)
words = text.split()
license_no = 'NA'
Name = words[words.index("Name")+1]+' '+words[words.index("Name")+2]
for word in words:
    if len(word)==16 and word[3:].isdigit():
        license_no = word


print(f'The license no: {license_no}')
print(f'The Name: {Name}')
cv2.imshow("Result",threshed)

cv2.waitKey(0)