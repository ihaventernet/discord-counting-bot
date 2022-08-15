import keyboard
# cv2.cvtColor takes a numpy ndarray as an argument
import numpy as nm  
import pytesseract
# importing OpenCV
import cv2  
from PIL import ImageGrab
import time   
# Path of tesseract executable
pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'

while(True):
     # ImageGrab-To capture the screen image in a loop. 
    # Bbox used to capture a specific area.
    cap = ImageGrab.grab(bbox =(370, 915, 1000, 940))
    time.sleep(5)
    # Converted the image to monochrome for it to be easily 
        # read by the OCR and obtained the output String.
    tesstr = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
                lang ='eng')
    print(tesstr)
    num = int(tesstr)
    numtype = num + 1
    keyboard.write(str(numtype))
    keyboard.press_and_release('enter')


