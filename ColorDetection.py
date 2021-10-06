import cv2
import numpy as np

path = 'Ressources/banana.png'
img = cv2.imread(path)

imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


cv2.namedWindow('Original',cv2.WINDOW_NORMAL)
cv2.imshow("Original",img)
cv2.resizeWindow('Original', 500,700)

cv2.namedWindow('HSV',cv2.WINDOW_NORMAL)
cv2.imshow("HSV",imgHSV)
cv2.resizeWindow('HSV', 500,700)

cv2.waitKey(0)
