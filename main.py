import keyboard
import numpy as nm  
import pytesseract
import cv2  
from PIL import ImageGrab
import time   
pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#coodinate of avatar pixel
x=340
y=913
#RGB value of pixel
red=234
green=141
blue=150
#coodinate for bbox
x1=370
y1=913
x2=1000
y2=940

while True :
    #avatar loop
    time.sleep(1)
    im = ImageGrab.grab(bbox=(x, y, x+1, y+1))
    rgbim = im.convert('RGB')
    r,g,b = rgbim.getpixel((0,0))
    if(r,g,b) == (red, green, blue):
        continue
    cap = ImageGrab.grab(bbox =(x1, y1, x2, y2))
    tesstr = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
            config="-c tessedit_char_whitelist=0123456789")
    if(tesstr) == "":
        continue
    num = int(tesstr)
    numtype = num + 1
    #write number
    keyboard.write(str(numtype))
    keyboard.press_and_release('enter')
