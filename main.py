import keyboard
import numpy as nm  
import pytesseract
import cv2  
from PIL import ImageGrab
import time   
pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#put rgb value of avatar pixel here
red=234
green=141
blue=150
#put x&y coodinate here
x1=370
y1=913
x2=1000
y2=940

while True :
    #delay added because of timestop lol
    time.sleep(2)
    im = ImageGrab.grab(bbox=(x1-30, y1, x1-29, y1+1))
    rgbim = im.convert('RGB')
    r,g,b = rgbim.getpixel((0,0))
    if(r,g,b) == (red, green, blue):
        continue
    cap = ImageGrab.grab(bbox =(x1, y1, x2, y2))
    gry = cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY)
    inverted_image = cv2.bitwise_not(gry)
    tesstr = pytesseract.image_to_string(inverted_image,
            config="-c tessedit_char_whitelist=0123456789, --psm 7")
    if(tesstr) == "":
        continue
    num = int(tesstr)
    if num == 1:
        numtype = num + 11
        keyboard.write(str(numtype))
        keyboard.press_and_release('enter')
        continue
    numtype = num + 1
    keyboard.write(str(numtype))
    keyboard.press_and_release('enter')
    if numtype % 100 == 11:
        if(r,g,b) == (red, green, blue):
            continue
        time.sleep(2)
        numtype = num + 3
        keyboard.write(str(numtype))
        keyboard.press_and_release('enter')

    
