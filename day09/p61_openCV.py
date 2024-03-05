#file: p61_openCV.py
#desc: OpenCV 영상 처리

import cv2

samplePath = './day09/earth.mp4'
cap = cv2.VideoCapture(samplePath)   #0(웹캠) or 문자열로 동영상 경로 입력

while True:
    ret, frame = cap.read()

    if not ret:
        cap = cv2.VideoCapture(samplePath)
        continue

    #영상 편집
    blur = cv2.blur(frame, (10, 10))
    flip = cv2.flip(frame, 0)
    
    cv2.imshow('original', frame)
    cv2.imshow('blur', blur)
    cv2.imshow('flip', flip)

    key = cv2.waitKey(5)    #5초 딜레이    
    if key == ord('q'):   #27 = esc, q = ord('q')
        break
    elif key == ord('c'):
        cv2.imwrite('./day09/capt.jpg', frame)  #c 누르면 캡쳐됨

cap.release()
cv2.destroyAllWindows()
