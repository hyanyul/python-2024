#file: p45.threadApp.py
#desc: PyQt5 스레드 학습용(스레드 사용)

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class BackgroundWorker(QThread):    #PyQt용 스레드
    initUiSignal = pyqtSignal(int)  #스레드로 진행할 때 UI에서 초기화 부분을 시그널로 전달
    setPgbSignal = pyqtSignal(int)  #스레드 진행 시 변경되는 숫자값을 UI로 전달
    setTxbSignal = pyqtSignal(str)  #스레드 진행 시 화면에 출력될 문자열을 UI쪽으로 전달

    def __init__(self, parent) -> None: #부모는 qtApp 클래스
        super().__init__(parent)
        self.parent = parent    #전역함수 parent 만들어서 parent 연결

    def run(self) -> None:
        maxVal = 1_000
        self.initUiSignal.emit(maxVal) #값 보내면 UI쪽(qtApp class)에서 받아서 처리하게 함 / emit: 전송 함수
        for i in range(maxVal):
            print(f'스레드 진행 >> {i}')    #콘솔에 찍히는 거 == ui 아니라 상관 없음
            self.setPgbSignal.emit(i)
            self.setTxbSignal.emit(f'스레드 진행 >> {i}')
            # self.parent.pgbTask.setValue(i) #UI 스레드의 권한을 일반 백그라운드에게 주지 않음 
            # self.parent.txbLog.append(f'스레드 진행 >> {i}')    #사용 불가


class qtApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self):
        uic.loadUi('./day07/testThread.ui', self)
        self.setWindowTitle('스레드앱')
        self.setWindowIcon(QIcon('./images/windows.png'))

        #버튼 시그널 처리
        self.btnStart.clicked.connect(self.btnStartClicked)

        self.show() 

    def btnStartClicked(self):
        self.btnStart.setDisabled(True)
        th = BackgroundWorker(self) #qtApp이 부모 클래스라고 선언
        th.start()  #스레드 안에 있는 run() 함수 실행
        th.initUiSignal.connect(self.initPgbTask)
        th.setPgbSignal.connect(self.setPgbTask)
        th.setTxbSignal.connect(self.setTxbLog)

        self.btnStart.setEnabled(True)

    @pyqtSlot(str)
    def setTxbLog(self, msg):
        self.txbLog.append(msg)
    
    @pyqtSlot(int)
    def setPgbTask(self, val):
        self.pgbTask.setValue(val)

    @pyqtSlot(int)  #pyqt Signal에서 넘어온 값을 처리해주는 부분이라고 선언
    def initPgbTask(self, maxVal):
        self.pgbTask.setValue(0)
        self.pgbTask.setRange(0, maxVal - 1)

    def closeEvent(self, QCloseEvent) -> None:  
        re = QMessageBox.question(self, '종료 확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: 
            QCloseEvent.accept()
        else:   
            QCloseEvent.ignore()

app = QApplication(sys.argv)    
inst = qtApp() 
app.exec_()