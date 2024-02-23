#file: p19_fileRead.py
#desc: 텍스트 파일 읽기

f = open('./day03/CHANGELOG.md', mode='r', encoding='utf-8')

while True:
    read = f.readline()    #한줄씩 읽어옴
    if not read:    #더 이상 읽을 값이 없으면 반복문 탈출
        break
    print(read.replace('\n',''))

f.close()
