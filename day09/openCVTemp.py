#file: openCVTemp.py
#desc: OpenCV 탬플릿

import cv2

image = cv2.imread('./day09/cat.jpg')

height, width, channel = image.shape

cv2.imshow('Cat', image)    #원본

cv2.waitKey(0)
cv2.destroyAllWindows()
