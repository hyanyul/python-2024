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
    
    def isNameExist(self, name):    #__name에 접근할 수 있는 함수 만듦, 연락처 여부 확인
        if self.__name == name:
            return True
        else:
            return False
    
    def getInfo(self):  #튜플 형태로 데이터 전달
        return self.__name, self.__phoneNumber, self.__eMail, self.__addr
    

def setContact():   #키보드로 입력 받아서 변수 초기화해주는 역할
    (name, phoneNum, eMail, addr) = input('정보 입력(이름, 전화번호, 이메일, 주소)[구분자: /]: ').split('/')
    name.strip()   #사용자가 스페이스 입력하더라도 없애서 정상적으로 입력되게 하는 역할
    phoneNum.strip()
    eMail.strip()
    addr.strip()
    #print(name, phoneNum, eMail, addr)
    contact = Contact(name, phoneNum, eMail, addr)
    return contact

def clearConsole():     #메뉴를 선택할 때마다 콘솔을 클리어한 뒤 화면 전환하는 기능
    command = 'clear'   #macOS, Linux, Unix 명령어
    if os.name in ('nt', 'dos'):    #window
        command = 'cls' #window 명령어
    os.system(command)

def getMenu():  #메뉴 출력
    strMenu = ('주소록 프로그램 v1.0\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 종료\n')
    print(strMenu)
    try:
        menu = int(input('메뉴 입력: '))
    except:
        menu = 0
    return menu

def getContact(lstContact):     #리스트를 받아서 출력하는 함수
    for i, item in enumerate(lstContact):  #enumerate(): 인덱스와 원소로 이루어진 튜플 만들어줌
        print(f'{i+1}-------------')
        print(item)

def delContact(lstContact, name):   #연락처 삭제 함수, 동명이인 함께 지워짐
    for i in range(len(lstContact)-1, -1, -1):  #리스트를 내림차순으로 뒤에서부터 삭제
        item = lstContact[i]
        if item.isNameExist(name):
            del lstContact[i]

def saveContact(lstContact):    #연락처 저장
    with open('./contact.txt', mode='w', encoding='utf-8') as fp:    #with: close 필요 없음  
        for item in lstContact:
            name, phoneNumber, eMail, addr = item.getInfo()
            fp.write(f'{name}/{phoneNumber}/{eMail}/{addr}\n')

def loadContact(lstContact):    #처음 실행 시 연락처 불러오는 함수
    try:
        with open('./contact.txt', mode='r', encoding='utf-8') as fp:
            while True:
                line = fp.readline()
                if not line:
                    break
            
                lines = line.replace('\n','').split('/')
                contact = Contact(lines[0], lines[1], lines[2], lines[3])
                lstContact.append(contact)
    except:     #연락처 파일이 없으면 새로 하나 만들어줌
        f = open('./contact.txt', mode='w', encoding='utf-8')
        f.close()

def run():
    lstContact = []
    loadContact(lstContact)    #연락처 로드

    clearConsole()     #화면 클리어

    while True:    #계속해서 메뉴 선택할 수 있도록 반복문 사용
        selMenu = getMenu()
        if selMenu == 1:
            clearConsole()
            try:
                contact = setContact()
            except:  #입력에 문제있을 때
                contact = None
            if contact != None: 
                lstContact.append(contact) 
                input('\n입력 성공')
            else:
                input('\n입력 실패')

            clearConsole()

        elif selMenu == 2:
            clearConsole()
            getContact(lstContact)
            input('\n출력 성공'); clearConsole()

        elif selMenu == 3:
            clearConsole()
            name = input('삭제할 이름을 입력하세요: ')
            delContact(lstContact, name)
            input('\n삭제 성공'); clearConsole()

        elif selMenu == 4:  #메뉴 4 눌렀을 때 종료 가능하도록 break
            saveContact(lstContact)
            break
     
if __name__ == '__main__':  #메인 엔트리
    run()

print('프로그램 종료')
