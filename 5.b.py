
import cv2
#weight of image 3 is 0.4 and wight of image 4 is 0.6

img1 = cv2.imread('3.jpg')
img2 = cv2.imread('4.jpg')
imgres = cv2.addWeighted(img1, 0.4, img2, 0.6, 0)
cv2.imshow('image', imgres)
cv2.waitKey(0)
cv2.distroyAllWindows()


