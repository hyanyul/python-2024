#file: p48. transApp.py
#desc: PyQt5 구글번역 앱

# >pip install googletrans
#모듈, 라이브러리 설치 시 버전 업/다운
# >pip install googletrans==3.1.0a0
# >pip install googletrans==4.0.0rc1 

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from googletrans import Translator


class qtApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.myTrans = Translator()
    
    def initUI(self):
        uic.loadUi('./day07/transApp.ui', self)
        self.setWindowTitle('구글 번역 앱')
        self.setWindowIcon(QIcon('./images/translate.png'))

        #버튼 시그널 처리
        self.btnTrans.clicked.connect(self.btnTransClicked)
        self.txtBaseText.returnPressed.connect(self.btnTransClicked)
        self.show() 

    def btnTransClicked(self):
        #QMessageBox.about(self, '번역', '번역 시작')
        text = self.txtBaseText.text().strip()
        if len(text) != 0:
            result = self.myTrans.translate(text, src='auto', dest='en')
            self.txbResult.append(result.text)

    def closeEvent(self, QCloseEvent) -> None:  
        re = QMessageBox.question(self, '종료 확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: 
            QCloseEvent.accept()
        else:   
            QCloseEvent.ignore()

app = QApplication(sys.argv)    
inst = qtApp() 
app.exec_()