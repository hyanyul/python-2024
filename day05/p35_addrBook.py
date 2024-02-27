#file: p34_addrBook.py
#desc: 콘솔 주소록 프로그램

import email
import os

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
                   f'주  소: {self.__addr}\n')
         return strRes  #주소값 리턴
    
    def isNameExist(self, name):    #__name에 접근할 수 있는 함수 만듦
         if self.__name == name:
              return True
         else:
              return False
         
    def getName(self):
         return self.__name
    
    def getPhoneNumber(self):
         return self.__phoneNumber
    
    def getEmail(self):
         return self.__eMail
    
    def getAddr(self):
         return self.__addr
    

def setContact():   #키보드로 입력 받아서 변수 초기화해주는 역할
     name, phoneNum, eMail, addr = input('정보 입력(이름, 전화번호, 이메일, 주소)[구분자: /]: ').split('/')
     name.strip()   #사용자가 스페이스 입력하더라도 없애서 정상적으로 입력되게 하는 역할
     phoneNum.strip()
     eMail.strip()
     addr.strip()
     #print(name, phoneNum, eMail, addr)
     contact = Contact(name, phoneNum, eMail, addr)
     return contact

def clearConsole():     #메뉴를 선택할 때마다 콘솔을 클리어한 뒤 화면 전환하는 기능
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def getMenu():  #메뉴 출력
     strMenu = ('주소록 프로그램 v1.0\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 종료\n')
     print(strMenu)
     menu = input('메뉴 입력: ')
     return int(menu)

def getContact(lstContact):
     for item in lstContact:
          print(item)

def delContact(lstContact, name):
     for i, item in enumerate(lstContact):
        if item.isNameExist(name):
             del lstContact[i]

def saveContact(lstContact):
     f = open('./day05/db_contact.txt', mode='wt', encoding='utf-8')
     for item in lstContact:
          f.write(item.getName() + '/')
          f.write(item.getPhoneNumber() + '/')
          f.write(item.getEmail() + '/')
          f.write(item.getAddr() + '\n')
     f.close()

def loadContact(lstContact):
     f = open('./day05/db_contact.txt')
     while True:
          line = f.readline()
          if not line:
               break
          
          lines = line.split('/')
          contact = Contact(lines[0], lines[1], lines[2], lines[3])
          lstContact.append(contact)
     f.close()

def run():
     lstContact = []

     clearConsole()

     while True:    #계속해서 메뉴 선택할 수 있도록 반복문 사용
          selMenu = getMenu()
          if selMenu == 1:
               clearConsole()
               contact = setContact()
               lstContact.append(contact) 
               input()
               clearConsole()  

          elif selMenu == 2:
               clearConsole()
               getContact(lstContact)
               input()
               clearConsole()

          elif selMenu == 3:
               clearConsole()
               name = input('삭제할 이름을 입력하세요: ')
               delContact(lstContact, name)
               input()
               clearConsole()

          elif selMenu == 4:  #메뉴 4 눌렀을 때 종료 가능하도록 break
               saveContact(lstContact)
               break
     
if __name__ == '__main__':  #메인 엔트리
    run()

print('프로그램 종료')