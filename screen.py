from PIL import ImageGrab
from tkinter import * 
from tkinter import messagebox
#use to calibrate input image 
#x1,y1: coodinate of top left corner 
#x2,y2 coodinate of bottom right corner
x1=370
y1=913
x2=1000
y2=940
#screenshot
im2 = ImageGrab.grab(bbox = (x1, y1, x2, y2))
im2.show()
#coodinate and rgb value of avatar pixel
im = ImageGrab.grab(bbox=(x1-30, y1, x1-29, y1+1))
rgbim = im.convert('RGB')
r,g,b = rgbim.getpixel((0,0))
red = str(r)
green = str(g)
blue = str(b)
rgb = red + " " + green + " " + blue
messagebox.showinfo("rgb value", rgb)