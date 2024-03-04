#file: p54_captWeather.py
#desc: 네이버 날씨화면 캡쳐

import pyautogui as auto
import pyperclip as clip
import time

regions = ['서울', '강원', '대전', '대구', '부산']

for region in regions:
    # auto.mouseInfo()
    auto.moveTo(200, 150, duration=0.5)
    auto.click(clicks=3, interval=0.1, button='left')   #기존에 있는 검색어 삭제
    auto.press('del')
    time.sleep(0.2)

    clip.copy(f'{region} 날씨')
    auto.hotkey('ctrl', 'v')
    time.sleep(0.2)

    auto.press('\n')    #'\n'=='enter'

    time.sleep(1.0)

    #30, 280 / 696, 909

    startX, startY = 30, 280
    endX, endY = 696, 909

    auto.screenshot(f'./day08/{region}_날씨.png', region=(startX, startY, endX-startX, endY-startY))