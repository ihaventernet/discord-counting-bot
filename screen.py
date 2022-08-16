from PIL import ImageGrab
#use to calibrate input image 
#x1,y1: coodinate of top left corner 
#x2,y2 coodinate of bottom right corner
x1=370
y1=913
x2=1000
y2=940
im2 = ImageGrab.grab(bbox = (x1, y1, x2, y2))
im2.show()