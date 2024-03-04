#file: p49_mouseAuto.py
#desc: PyAutoGui 로 마우스 설치

'''
파이썬 모듈 설치 시 명령 프롬프트보다 VSCode 내 터미널에서 설치 추천
PyAutoGui 모듈 설치
>pip install pyautogui
'''

import pyautogui as auto

print(auto.size())  #현재 모니터 해상도 정보(주모니터)  Size(width=1920, height=1080)
print(auto.position())  #현재 마우스 커서의 위치 나타냄

#pyautogui 마우스 설정창
#pip install pillow(pillow 모듈) 필요 -> 마우스 커서 갖다대는 곳 색깔 뜸
# auto.mouseInfo()

# 마우스 이동(절대 좌표)
# auto.moveTo(100, 51)
# auto.moveTo(1811, 761, duration=1.0)    #duration: 마우스 커서 이동 시간 조정
# auto.moveTo(1210,568, duration=0.1)

#상대 좌표 마우스 이동(현재 위치에서 이동)
# auto.move(50, 50, duration=1.5) #현재 위치에서 x축 50, y축 50만큼 1.5초동안 이동

#마우스 클릭
# auto.click()
# auto.leftClick(x=1811, y=761)   #해당 좌표로 가서 바로 왼쪽 클릭
# auto.rightClick(x=1811, y=761, duration=1.5)
# auto.click(clicks=4, interval=0.1, button='left')   #왼쪽 버튼을 소스코드 에디터에서 4번 클릭하면 모든 글 전체 선택됨

# #마우스 드래그
# auto.leftClick(x=1430, y=235, duration=1.0) #1430, 235로 1초간 이동 후 왼쪽 마우스 클릭
# auto.dragTo(x=1300, y=636,duration=2.0, button='left')

# auto.dragRel(500, 400, duration=1.0, button='left') #현재 위치에서 500, 400만큼 1초동안 드래그

#마우스 휠
auto.scroll(200)    #양수는 위로
auto.scroll(-100)   #음수는 아래로 스크롤

