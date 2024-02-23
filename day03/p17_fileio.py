#file: p17_fileio.py
#desc: 파일 입출력 학습

#컴퓨터에서 열면 무조건 닫아야 하는 것
# 1. 파일 open(), close()   #파이썬에서만 안 닫아도 크게 지장 없음
# 2. 네트워크 통신 open(), close()  #네트워크 통신: 개수 정해져 있음->다 쓴 건 닫아줘야 여분이 생김
# 3. DB open() or connect(), close()    #개수 정해져 있음

#언어 체계 추가 / 기본: 아스키코드(ASCII-한글: cp949), 유니코드(UTF-8)
#상대 경로, 절대 경로(중요!)
#mode w: 매번 새로 파일 생성, a: 기존 파일에 내용 추가, r: 파일 읽기
#log 등을 남길 때는 a 사용해야 함
f = open('./day03/sample.txt', mode = 'w', encoding = 'UTF-8')  #.: 자기 자신을 가리킴(상대경로)

#파일 쓰기 진행
f.write('안녕하세요. 파이썬\n')     #write(): 개행x, 개행하고 싶으면 이스케이프 문자(\n) 사용
f.write('모두 화이팅!!\n')

#파일 닫기
f.close()   #파이썬에서는 없어도 됨(옵션), 다른 언어에서는 필수
