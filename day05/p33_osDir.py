#file: p33_osDir.py
#desc: 운영체제 디렉토리 확인

import os   #운영체제에서 필요한 모듈

def search(dirName):
    try:
        fileNames = os.listdir(dirName)     #결과로 list 나옴
        for fileName in fileNames:
            fullName = os.path.join(dirName, fileName)      #str로 나옴
            if os.path.isdir(fullName):     #하위 디렉토리 있을 경우, os.path.isdir(fullName): True, False로 나옴
                search(fullName)    #재귀호출 
            else:
                #ext = os.path.splitext(fullName)        #확장자가 튜플 형태로 출력됨
                ext = os.path.splitext(fullName)[-1]    #확장자만 나옴
                if ext == '.py':    #파이썬 파일만 출력, *.ipynd: 주피터 노트북 확장자
                    with open(fullName, mode='r', encoding='utf-8') as fp:      #with로 파일 열면 close() 필요 없음
                        print(f'파일명: {fullName}, 라인 수: {len(fp.readlines())}줄')
    except PermissionError as e:    #PermissionError: 접근권한 없을 때 뜨는 에러
        print('접근 권한이 없습니다.', e.args)

if __name__ == '__main__':      #main entry
    search('C:/Source/python-2024')     #OS 드라이브 경로에서 \는 되도록 쓰지말 것
    