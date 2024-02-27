#file: p34_addrBook.py
#desc: 콘솔 주소록 프로그램

import email

class Contact:  #주소록 클래스
    def __init__(self, name, phoneNumber, eMail, addr) -> None:     #생성자
            self.__name = name
            self.__phoneNumber = phoneNumber
            self.__eMail = eMail
            self.__addr = addr

    def __str__(self) -> str:   #사용자가 원하는 형태로 출력
         strRes = (f'이  름: {self.__name}\n'       #원래 출력: 주소값 나옴
                   f'핸드폰: {self.__phoneNumber}\n'
                   f'이메일: {self.__eMail}\n'
                   f'주  소: {self.__addr}')
         return strRes
    

def setContact():
     name, phoneNum, eMail, addr = input('정보 입력(이름, 전화번호, 이메일, 주소)[구분자: /]: ').split('/')
     print(name, phoneNum, eMail, addr)

def getMenu():
     strMenu = ('주소록 프로그램 v1.0\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 종료\n')
     print(strMenu)
     menu = input('메뉴 입력: ')
     return int(menu)

def run():
     while True:
          selMenu = getMenu()
          if selMenu == 4:
               break
     
if __name__ == '__main__':  #메인 엔트리
    run()

print('프로그램 종료')
