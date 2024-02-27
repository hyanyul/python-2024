#file: p36_qtApp.py
#desc: PyQt5 앱 만들기

'''
PyQt -> Qt를 파이썬에서 쓸 수 있도록 만든 라이브러리
Qt -> C, C++ 사용할 GUI(WinApp) 프레임워크(멀티 플랫폼)

설치 > pip install PyQt5
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import * #QPaintEvent, QPainter
#QApplication: 만들 앱 전체를 관리하는 클래스 / QWidget: 메뉴가 없는 윈도우 앱 / QMainWindow: 메뉴가 있는 윈도우 앱
from PyQt5.QtWidgets import * #QApplication, QWidget, QMainWindow

class qtApp(QWidget):   #QWidget 클래스 상속받음->QWidget이 가진 변수, 함수 모두 사용 가능
    def __init__(self) -> None: #생성자, 부모 클래스의 생성자 함수도 실행되어야 함
        super().__init__()
        self.initUI();
    
    def initUI(self):
        self.setGeometry(300, 300, 800, 400)    #바탕화면의 정해진 위치에 너비와 높이로 그릴지 설정
        self.setWindowTitle('첫번째 윈도우 앱')
        self.setWindowIcon(QIcon('./images/windows.png'))   #창 이름 옆에 아이콘 넣음
        self.show() #윈도우  창 그리는 역할
    
    def paintEvent(self, event) -> None:
        paint = QPainter()  #윈도우 창 위에 그림을 그리는 객체
        paint.begin(self)   #자기 자신에 그림 그리기 시작
        paint.setPen(QColor(200, 0, 0))  #RGB / dark red
        paint.setFont(QFont('Bauhaus 93', 40))    #영어로 적어줘야 함
        paint.drawText(255, 400//2, 'Hello PyQt!')
        paint.end() #반드시 닫아야 함(begin-end는 세트)

app = QApplication(sys.argv)    #argv: 필요 시 파라미터를 받아서 쓸 수 있음
inst = qtApp()  #객체 생성
app.exec_() #실행
