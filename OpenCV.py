import random
from tkinter import Frame
import cv2
from cv2 import dilate
from pynput import keyboard
import numpy
import random

org = cv2.imread("Media/Unicorn.jpg")
img = cv2.resize(org, (0,0), fx=0.6, fy=0.5)
vdo = cv2.VideoCapture("FRC.mp4")
cam = cv2.VideoCapture(0)  
canny = cv2.Canny(img, 50, 100)
kernal = numpy.ones((3,3), numpy.uint8)

myfd = numpy.empty((64, 64, 3), numpy.uint8)
            #BGR channel=3 #Gray channel=1 #8位無符號整數
for row in range(64):
    for col in range(64):
        myfd[row][col]= [int(random.randint(0, 255)), int(random.randint(0, 255)),int(random.randint(0, 255))]
#B G R

def empty(v):
        pass
cv2.namedWindow("bartander")
cv2.resizeWindow("bartander", 320, 100)
cv2.createTrackbar("Satu_Min", "bartander", 0,1000, empty)
cv2.createTrackbar("Satu_Max", "bartander", 0,1000, empty)
"""
while True:
    lower = cv2.getTrackbarPos("Satu_Min", "bartander")
    upper = cv2.getTrackbarPos("Satu_Max", "bartander")
    
    cv2.imshow("canny_md", canny_md)
    cv2.waitKey(1)"""

while True:
  ret, frame = cam.read()# .read() return(boolean, each frame that is returned)
  if ret:
      frame = cv2.resize(frame, (0,0), fx=1.5, fy=1.5)
      frameflip = cv2.flip(frame, 1)

      lower = cv2.getTrackbarPos("Satu_Min", "bartander")
      upper = cv2.getTrackbarPos("Satu_Max", "bartander")
      canny_md = cv2.Canny(frameflip, int(lower), int(upper))
      inflate = cv2.dilate(canny_md, kernal, iterations=1)
      cv2.namedWindow("frameflip", cv2.WINDOW_NORMAL)
      cv2.namedWindow("canny_md", cv2.WINDOW_NORMAL)
      # .namedWindow() create window; WINDOW_NORMAL capable to resize the window

      cv2.imshow("frameflip", frameflip)
      cv2.imshow("inflate", inflate)
      cv2.waitKey(1)# "0" represents infinitely 
  else:
      break
  if cv2.waitKey(10)& 0xFF == ord("q"):
    break


# cv2.namedWindow("img", cv2.WINDOW_NORMAL)
# 讓視窗可以自由縮放大小

# grayimg = cv2.imread("img", 0)
# cv2.imshow("grayimg", grayimg)

# cv2.imshow("img", img)
# cv2.imshow("org", org)
# cv2.imshow("myfd", myfd)
cv2.waitKey(0)
cv2.destroyAllWindows()

