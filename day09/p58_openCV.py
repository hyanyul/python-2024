#file: p58_openCV.py 
#desc: OpenCV 활용

#OpenCV: 실시간 이미지 프로세싱 라이브러리
'''
> pip install opencv-python
'''

import cv2

#print(cv2.__version__)  #OpenCV 설치 확인용

image = cv2.imread('./day09/cat.jpg')   #디폴트: IMREAD_UNCHANGED
#image = cv2.imread('./day09/cat.jpg', cv2.IMREAD_GRAYSCALE) #IMREAD_GRAYSCALE: 컬러->흑백으로 바꿈
#image = cv2.imread('./day09/cat.jpg', cv2.IMREAD_REDUCED_COLOR_2)   #크기 반으로 줄임
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #원본을 흑백으로 변경

height, width, channel = image.shape
print(height, width, channel)   #세로: 667, 가로: 1000, 채널: 3(바이트)

sizeSmall = cv2.resize(image, (width//2, height//2))    #크기 설정 시 정수만 가능

img_cropped = image[(height//2):, :(width//2)] #x축을 반으로 잘라 반만 나오도록 설정 / image(세로, 가로)

cv2.imshow('Cat, color', image) #원본
cv2.imshow('Cat, gray', gray)   #흑백
cv2.imshow('Reduced Cat', sizeSmall)    #원본의 1/4 사이즈(가로 세로 각각 반으로 줄임)
cv2.imshow('Half Cat', img_cropped)

cv2.waitKey(0)
cv2.destroyAllWindows() #나머지 필요없는 거 지움
