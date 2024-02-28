#file: p37_qtApp.py
#desc: PyQt5 앱 만들기(day05 p36 이어서)

'''
PyQt -> Qt를 파이썬에서 쓸 수 있도록 만든 라이브러리
Qt -> C, C++ 사용할 GUI(WinApp) 프레임워크(멀티 플랫폼)

설치 > pip install PyQt5
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import * 
#QMainWindow, QLabel, QPushButton 등은 QWidget을 상속한 자식 클래스(부모 클래스의 능력들을 다 사용할 수 있음)
from PyQt5.QtWidgets import* #QApplication, QWidget, QMainWindow, QLabel

class qtApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI();
    
    def initUI(self):
        label = QLabel()    #라벨 만듦, 라벨 위젯(qt, PyQt) == 라벨 컨트롤(MFC, C#, Java Fx, Android)

        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle('두번째 qt 앱')
        self.setWindowIcon(QIcon('./images/windows.png'))
        self.text = 'What a wonderful world.'   #== paintEvent()와 같은 효과
        label.setText(self.text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)    #알아서 정중앙에 배치됨->창 크기 키워도 알아서 정중앙에 위치
        #label.setAlignment(Qt.AlignmentFlag.AlignTop)  #왼쪽 위에 배치
        label.setStyleSheet('color: blue;'
                            'background-color: white;')   #라벨의 색상 스타일 설정 가능 / html css와 완전 동일

        font = label.font()
        font.setFamily('Bauhaus 93')    #글꼴 설정
        font.setPointSize(40)   #글자 크기 설정

        label.setFont(font)

        layout = QVBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)
        self.show() #윈도우 창 나타나게 하는 역할, 없으면 창 안뜸
    
    def paintEvent(self, event) -> None:
        paint = QPainter()
        paint.begin(self)  
        paint.setPen(QColor(200, 0, 0)) 
        paint.setFont(QFont('Bauhaus 93', 40))  
        paint.drawText(255, 400//2, 'Hello PyQt!')
        paint.end() 

app = QApplication(sys.argv)    
inst = qtApp() 
app.exec_() 
