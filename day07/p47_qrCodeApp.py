#file: p47. qrCodeApp.py
#desc: PyQt5 QRCode 앱

#pip install qrcode

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import qrcode

class qtApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self):
        uic.loadUi('./day07/qrApp.ui', self)
        self.setWindowTitle('QR 코드 생성기')
        self.setWindowIcon(QIcon('./images/qrCode.png'))

        #버튼 시그널 처리
        self.btnGenerate.clicked.connect(self.btnGenerateClicked)
        self.show() 

    def btnGenerateClicked(self):
        data = self.txtQrData.text()

        if len(data.strip()) == 0:
            QMessageBox.about(self, '경고', '데이터를 입력해주세요.')
            return
        else:
            imgPath = './day07/qr.png'
            qrImage = qrcode.make(data)
            qrImage.save('./day07/qr.png')
            img = QPixmap(imgPath)
            self.lblQrCode.setPixmap(QPixmap(img).scaledToWidth(300))

    def closeEvent(self, QCloseEvent) -> None:  
        re = QMessageBox.question(self, '종료 확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: 
            QCloseEvent.accept()
        else:   
            QCloseEvent.ignore()

app = QApplication(sys.argv)    
inst = qtApp() 
app.exec_()