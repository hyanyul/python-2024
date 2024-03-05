#file: p59_openCV.py
#desc: OpenCV 이미지 처리 계속

import cv2

image = cv2.imread('./day09/cat.jpg')   #원본
dst = cv2.flip(image, 1)    #0: 상하반전, 1: 좌우반전

height, width, channel = image.shape    #흑백: 1채널, 컬러: 3채널(RGB)
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, -1)  #90: 회전 각도, +: 반시계방향(ccw) / -: 시계방향(cw) / 숫자: 배율
thrd = cv2.warpAffine(image, matrix, (width, height))
reverse = cv2.bitwise_not(image)    #색상 반전
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)   #흑백
ret, bny = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) #이진화(0 or 1) - 검정 혹은 흰색으로 나옴

cv2.imshow('Cat', image)
cv2.imshow('Flip Cat', dst)
cv2.imshow('Rotation Cat', thrd)
cv2.imshow('Reverse color Cat', reverse)
cv2.imshow('Gray Cat', gray)
cv2.imshow('Binary Cat', bny)

cv2.waitKey(0)
cv2.destroyAllWindows()
