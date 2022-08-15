import keyboard
import numpy as nm  
import pytesseract
# importing OpenCV
import cv2  
from PIL import ImageGrab
import time 

x=340
y=913
im = ImageGrab.grab(bbox=(x, y, x+1, y+1))
rgbim = im.convert('RGB')
r,g,b = rgbim.getpixel((0,0))
print('rgb value: ',(r,g,b))