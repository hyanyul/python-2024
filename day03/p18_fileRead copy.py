#file: p18_fileRead.py
#desc: 텍스트 파일 읽기

f = open('./day03/CHANGELOG.md', mode='r', encoding='utf-8')
f2 = open('./day03/dest.txt', mode='w', encoding='utf-8')

read = f.readlines()    #readline: 한줄만 읽어옴, readlines: 모든 줄 다 읽어옴, 배열로 들고옴

print('파일에서 읽은 내용 > ', read)

for line in read:      # for문으로 한줄씩 읽어올 수 있음
    print(line, end = '')

print()

for line in read:
    print(line.replace('\n', ''))
    f2.write(line)     #텍스트 파일 카피(복사)-파일 읽어서 그대로 다른 파일에 쓰는 것

f.close()
f2.close()

