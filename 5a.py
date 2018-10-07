
import cv2

img1 = cv2.imread('3.jpg')
img2 = cv2.imread('4.jpg')
imgres = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
cv2.imshow('image', imgres)
cv2.waitKey(0)
cv2.distroyAllWindows() 
