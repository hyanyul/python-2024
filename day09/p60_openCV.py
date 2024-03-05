#file: p60_openCV.py
#desc: OpenCV 계속

import cv2

image = cv2.imread('./day09/cat.jpg')
dst = cv2.blur(image, (10,10), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
canny = cv2.Canny(image, 100,255)

height, width, channel = image.shape

cv2.imshow('Cat', image)    #원본
cv2.imshow('Blur Cat', dst) #블러
cv2.imshow('Sobel Cat', sobel)  #입체감 있는 윤곽
cv2.imshow('Laplacian Cat', laplacian)  #일반적인 윤곽
cv2.imshow('Canny Cat', canny)  #흑백으로 윤곽

cv2.waitKey(0)
cv2.destroyAllWindows()
