#file: p64_imageEditor.py
#desc: PyQt 이미지 에디터
'''
qrc 파일을 사용하려면
> pyrcc5 "resources.qrc" -o "resources_rc.py"
'''

import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QCloseEvent, QMouseEvent
from PyQt5.QtWidgets import *
import resources_rc #리소스 파일 추가
import cv2  #OpenCV 추가

class WinApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()

    def initUI(self):
        uic.loadUi('./day09/pyNewPaint.ui', self)
        self.setWindowIcon(QIcon('./day09/imgs/editor.png'))
        self.setWindowTitle('이미지 에디터')
        #이미지 추가 / 여러가지 UI에 대한 초기화
        pixmap = QPixmap('./day09/cat.jpg').scaledToHeight(471)
        self.lblCanvas.setPixmap(pixmap)
        self.brushColor = Qt.red    #빨간색 기본

        self.show()
    
    #메뉴/툴바 액션에 대한 시그널 처리 함수 정의
    def initSignal(self):
        self.action_New.triggered.connect(self.actionNewClicked)
        self.action_Open.triggered.connect(self.actionOpenClicked)
        self.action_Save.triggered.connect(self.actionSaveClicked)
        self.action_Exit.triggered.connect(self.actionExitClicked)
        self.action_Red.triggered.connect(self.actionRedClicked)
        self.action_Blue.triggered.connect(self.actionBlueClicked)
        self.action_Green.triggered.connect(self.actionGreenClicked)
        self.action_About.triggered.connect(self.actionAboutClicked)
        #변환 메뉴 추가
        self.actionGrayscale.triggered.connect(self.actionGrayscaleClicked)

    def actionNewClicked(self):
        canvas = QPixmap(self.lblCanvas.width(), self.lblCanvas.height())
        canvas.fill(QColor('white'))
        self.lblCanvas.setPixmap(canvas)

    def actionOpenClicked(self):
        image = QFileDialog.getOpenFileName(self, '이미지 열기', '', 'Image file(*.jpg;*.png;*.jpeg)')
        imagePath = image[0]
        pixmap = QPixmap(imagePath).scaledToHeight(471)
        self.lblCanvas.setPixmap(pixmap)
        self.lblCanvas.adjustSize()
    
    def actionSaveClicked(self):
        filePath, _ = QFileDialog.getSaveFileName(self, '이미지 저장', '', 'Image file(*.jpg;*.png)')
        if filePath == '':
            return
        pixmap = self.lblCanvas.pixmap()
        pixmap.save(filePath)

    def actionExitClicked(self):
        exit(0)

    def actionRedClicked(self):
        self.brushColor = Qt.red

    def actionGreenClicked(self):
        self.brushColor = Qt.green

    def actionBlueClicked(self):
        self.brushColor = Qt.blue

    def actionAboutClicked(self):
        QMessageBox.about(self, '정보', '이미지 에디터')

    def actionGrayscaleClicked(self):
        image = cv2.imread()

    def mouseMoveEvent(self, e) -> None:
        print(e.x(), e.y()-54)
        brush = QPainter(self.lblCanvas.pixmap())   #lblCanvas에 브러쉬 하나 생성
        brush.setPen(QPen(self.brushColor, 3.5, style=Qt.SolidLine, cap=Qt.RoundCap))
        brush.drawPoint(e.x(), e.y()-54)
        brush.end()
        self.update()   #화면 업데이트

    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = WinApp()
    sys.exit(app.exec_())
