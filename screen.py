# Importing Image and ImageGrab module from PIL package 
from PIL import Image, ImageGrab
import cv2   
import numpy as nm
# using the grab method
im2 = ImageGrab.grab(bbox = (370, 913, 1000, 940))
gry = cv2.cvtColor(nm.array(im2), cv2.COLOR_BGR2GRAY)    
filename =  "test.png"
cv2.imwrite(filename, gry)