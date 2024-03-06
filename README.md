# 빅데이터 언어 2024
빅데이터 자바 개발자 과정-파이썬 학습



## 1일차
- 파이썬 개발 환경 설정
    - [github](https://github.com/) 가입 
    - [git](https://git-scm.com/) 설치
    - [github 데스크탑](https://docs.github.com/ko/desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop)
    - [파이썬](https://www.python.org/) 설치
    - [Visual Studio Coad](https://code.visualstudio.com/) 설치
    - [나눔고딩코딩](https://github.com/naver/nanumfont) 글꼴 설치

- 파이썬 학습
    - 파이썬 개요
        - 1990년 네덜란드계 개발자 귀도 반 로섬이 개발
        - 특징: 쉽고 간결한 문법, 무료, 빠른 개발 속도
    - 파이썬 기초 문법
        - 숫자형(정수, 실수, 진수)
        ```python
        #변수만 선언, 값만 할당하면 숫자형으로 지정
        #c, c++, java, c#처럼 형 지정 없음
        val = 10                    #정수형
        val = 2.15                  #실수형

        #특수 숫자형(진수)
        binVal = 0b11111111         #255(2진수)  /  0, 1
        octVal = 0o11               #9(8진수)  /  1~7
        hexVal = 0xFF               #255(16진수)  /  0~9ABCDEF
        print('2진수:', binVal, '/ 8진수:', octVal, '/ 16진수:', hexVal)
        ```
        - 문자열형(연산, 포매팅, 함수)
        ```python
        #'', "" 모두 사용 가능
        ```
        - 리스트형, 튜플형(연산, 함수)
            - 리스트: 수정, 삭제 가능
            - 튜플: 수정, 삭제 불가(그 외에는 리스트와 동일)


## 2일차
- 파이썬 학습
    - 파이썬 기초 문법
        - 딕셔너리, 집합
        - 불형
        - None형
        - 제어문(if, for, while)
        - 제어문 연습
        - 함수
    

## 3일차
- 파이썬 학습
    - 파이썬 기초 문법
        - 입출력
        - 객체 지향
        

## 4일차
- 파이썬 학습
    - 파이썬 기초 문법
        - 모듈, 패키지
        - ★예외처리, 디버깅☆: 디버깅하면서 예외 찾고, 거기에 예외처리
        - 내장 함수
        - 표준 및 외부 라이브러리


## 5일차
- 파이썬 학습
    - 파이썬 응용
        - OS 내 디렉토리 검색
        - 아스키 및 유니코드
        - 주소록 앱 만들기
        ```python
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
        ```
        ![주소록 앱](https://github.com/hyanyul/python-2024/blob/main/images/bigdata01.gif?raw=true)
        
        - Window App 만들기(PyQt)
        ![Window App](https://github.com/hyanyul/python-2024/blob/main/images/bigdata02.png?raw=true)


## 6일차 (2024.02.28)
- 파이썬 학습
    - 파이썬 응용
        - PyQt5 학습
            - QWidget 자식 클래스 종류 학습
            ![QLabel](https://github.com/hyanyul/python-2024/blob/main/images/bigdata03.png?raw=true)
            
            - Naver 뉴스 API 검색 앱
            ![네이버 뉴스 검색 앱](https://github.com/hyanyul/python-2024/blob/main/images/bigdata04.png?raw=true)


## 7일차
- 파이썬 학습
    - PyQt5 학습
        - Naver 뉴스 API 검색 앱 마무리
    - json 학습 
    - PyQt5
        - 스레드 개념, 학습
        ![스레드](https://github.com/hyanyul/python-2024/blob/main/images/bigdata05.png?raw=true)

- 파이썬 응용
    - TTS
    - QRCode 생성기
    ![QR](https://github.com/hyanyul/python-2024/blob/main/images/bigdata06.png?raw=true)
    - 구글번역기앱
    ![구글번역](https://github.com/hyanyul/python-2024/blob/main/images/bigdata07.png?raw=true)


## 8일차
- 파이썬 응용
    - 파이썬 자동화
        - PyAutoGui 모듈(마우스, 키보드, 화면 캡쳐) 
        - 슬랙 webhook로 모바일 메시지 전송
        <!--![슬랙](https://github.com/hyanyul/python-2024/blob/main/images/bigdata08.png?raw=true)-->
        <!--html 태그로 이미지 삽입 시 문제 없음-->
        <img src="https://github.com/hyanyul/python-2024/blob/main/images/bigdata08.jpg?raw=true" width="250">
        
        - Tesseract 프로그램으로 이미지에서 글자 추출(인식률 높이기 위해서는 직접 트레이닝해서 트레이닝 데이터 만들어야 함)
        ![테서렉트](https://github.com/hyanyul/python-2024/blob/main/images/bigdata09.png?raw=true)


## 9일차
- 파이썬 응용
    - 이미지 처리 OpenCV
    ![얼굴인식](https://github.com/hyanyul/python-2024/blob/main/images/bigdata10.gif?raw=true)

    - [Flask](https://flask-docs-kr.readthedocs.io/ko/latest/index.html), [Django](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django) 웹서버

    - 그림 에디터 만들기(with PyQt5)
    ![그림에디터](https://github.com/hyanyul/python-2024/blob/main/images/bigdata11.png?raw=true)


## 10일차
- 파이썬 응용
    - 그림 에디터 완성(OpenCV 그레이 스케일, 블러 처리)
    - mp4로 동영상(10MB 이하) 업로드 하려면  깃허브 사이트에서  README.md를 수정 후 mp4 드래그하면 가능
    - 실행파일 만들기
        - PyInstall
        ```shell
        > pip install pyinstaller
        > pyinstaller -w -F pythonfile.py
        ```
        - -w: 윈도우창만 실행되고 콘솔창 삭제
        - -F: _internal 폴더 생성 안되도록 진짜 oneFile로 만들어주는 옵션
        - 실패, 재생성 시 폴더에 있는 build, dist 폴더, 같은 파일이름.spec 삭제 뒤 다시 명령어 실행
        ![그림에디터](https://github.com/hyanyul/python-2024/assets/158116933/cd5e3a38-69d4-4bcb-899a-82a601b1ebd3)

    - Jupyter Notebook 사용법(빅데이터 분석, 코딩테스트)
<<<<<<< Updated upstream
    - 메모장 만들기
=======
        - Ctrl + Shift + P (명령 팔레트)
        - 노트북 사용
    
    - 메모장 만들기
>>>>>>> Stashed changes
