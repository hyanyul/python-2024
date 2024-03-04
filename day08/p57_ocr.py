#file: p57_ocr.py
#desc: 이미지 내 글자 인식

'''
> pip install pytesseract
'''

from PIL import Image
import pytesseract as pt

imgPath = './day08/originalImage.png'
im = Image.open(imgPath)
im.show()

pt.pytesseract.tesseract_cmd = 'C:\DEV\Tessoract-OCR/tesseract.exe' #테서렉트 설치 경로 입력
text = pt.image_to_string(Image.open(imgPath), lang='kor')

print(text) #인식 잘 안됨
