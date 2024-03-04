#file: p50_keyboardAuto.py
#desc: 키보드 자동화 with PyAutoGui

'''
한글 입력은 pyperclip
> pip install pyperclip #설치돼있음
'''

import pyautogui as auto
import pyperclip as clip

# auto.mouseInfo()
# auto.click(485, 591)
# auto.write("print('Hello, Python!')", interval=0.01) #0.2초에 한글자씩 입력
# auto.write("\n", interval=0.01)
# auto.write(['H', 'e', 'l', 'l', 'o', '!', '!'], interval=0.1)
# auto.write("\n", interval=0.01)
# auto.typewrite("print('Life is short, you need python.')", interval=0.01)    #write와 동일

#키보드 프레스 기능
auto.press('enter')
# auto.press('A')

#키보드 단축키로 입력
# auto.hotkey('ctrl', 'a')    #전체 선택
# auto.hotkey('ctrl', 'c')    #복사
# auto.press('esc')

# auto.press('\n')
# auto.press('\n')
# auto.press('\n')

# auto.hotkey('ctrl', 'v')

# auto.write('안녕하세요. 파이썬입니다.') #한글 입력 안됨

clip.copy('안녕하세요. 파이썬입니다.')  #클립보드에 복사해놓음
auto.hotkey('ctrl', 'v')    #붙여넣기


