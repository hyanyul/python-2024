#file: p64_imageEditor.py
#desc: PyQt 이미지 에디터
'''
qrc 파일을 사용하려면
> pyrcc5 "resources.qrc" -o "resources_rc.py"
> pip install imutils
'''

import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QCloseEvent, QMouseEvent
from PyQt5.QtWidgets import *
import resources_rc #리소스 파일 추가
import cv2, imutils  #OpenCV, imutils 추가

class WinApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()

    def initUI(self):
        # uic.loadUi('./day09/pyNewPaint.ui', self)   # VSCode 실행용
        uic.loadUi('C:/Source/python-2024/day09/pyNewPaint.ui', self)   # PyInstaller용 절대경로
        # self.setWindowIcon(QIcon('./day09/imgs/editor.png'))
        self.setWindowIcon(QIcon('C:/Source/python-2024/day09/imgs/editor.png'))  #절대경로
        self.setWindowTitle('이미지에디터  v0.5')
        ## 이미지 추가 / 여러가지 UI에 대한 초기화
        # pixmap = QPixmap('./day09/cat.jpg').scaledToHeight(471)
        pixmap = QPixmap('cat.jpg').scaledToHeight(471)
        self.lblCanvas.setPixmap(pixmap)
        self.brushColor = Qt.red    # 빨간색이 기본
        ## UI 초기화 끝
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
        self.actionBlur.triggered.connect(self.actionBlurClicked)

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
        cv2.destroyAllWindows()
        exit(0)

    def actionRedClicked(self):
        self.brushColor = Qt.red

    def actionGreenClicked(self):
        self.brushColor = Qt.green

    def actionBlueClicked(self):
        self.brushColor = Qt.blue

    def actionAboutClicked(self):
        QMessageBox.about(self, '정보', '이미지 에디터')

    def actionBlurClicked(self):
        tmpPath = './temp.png'
        pixmap = self.lblCanvas.pixmap()
        pixmap.save(tmpPath)
        image = cv2.imread(tmpPath)
        blur = cv2.blur(image, (10, 10))
        blurImg = QImage(blur, blur.shape[1], blur.shape[0], blur.strides[0], QImage.Format_BGR888)
        self.lblCanvas.setPixmap(QPixmap.fromImage(blurImg))

    def actionGrayscaleClicked(self):
        #<순서>
        #temp.png와 같은 형태로 이미지를 임시 저장
        #저장한 이미지 openCV로 불러옴
        #그레이 스케일로 변경
        #lblCanvas에 pixmap으로 변환
        #lblCanvas에 올림
        tmpPath = './day09/temp.png'
        pixmap = self.lblCanvas.pixmap()    #라벨이 있는 그림을 pixmap 변수에 저장
        pixmap.save(tmpPath)
        image = cv2.imread(tmpPath) #tmpPath로 이미지 읽어옴
        grayImg = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_Grayscale16)
        self.lblCanvas.setPixmap(QPixmap.fromImage(grayImg))

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
            cv2.destroyAllWindows()
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = WinApp()
    sys.exit(app.exec_())
