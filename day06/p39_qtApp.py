#file: p39_qtApp.py
#desc: PyQt5, QtDesigner를 같이 사용

'''
설치 > pip install PyQt5
설치 > pip install PyQt5Designer
시그널 == 이벤트
위젯 == 컨트롤
'''

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class qtApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self):   #ui 파일을 로드해서 화면 디자인 사용
        uic.loadUi('./day06/firstApp.ui', self)
        self.setWindowIcon(QIcon('./images/windows.png'))

        #버튼 시그널 처리
        self.btnMsg.clicked.connect(self.btnMsgClicked) #ui 파일 내 위젯은 자동완성 안됨(실행 시 불러오기 때문)

        self.show() 

    def btnMsgClicked(self):
        self.label.setText('What the *')
        QMessageBox.about(self, 'Qt 디자이너', '클릭하였습니다.')
        

    def closeEvent(self, QCloseEvent) -> None:  
        re = QMessageBox.question(self, '종료 확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: 
            QCloseEvent.accept()
        else:   
            QCloseEvent.ignore()

app = QApplication(sys.argv)    
inst = qtApp() 
app.exec_() 
