# Importing Image and ImageGrab module from PIL package 
from PIL import Image, ImageGrab
    
# using the grab method
im2 = ImageGrab.grab(bbox = (370, 915, 1000, 940))
    
im2.show()