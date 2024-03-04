#file: p54_katalkAuto.py
#desc: 카톡 PC에서 자동으로 메시지 보내기

import pyautogui as auto
import pyperclip as clip
import os
import time 

katalkLoc = auto.locateOnScreen('./day08/findLoc.png')
print(katalkLoc)
clickPos = auto.center(katalkLoc)
auto.doubleClick(clickPos)

# clip.copy('파이썬에서 자동으로 보내는 메세지입니다.')
# auto.hotkey('ctrl', 'v')
# auto.press('\n')
