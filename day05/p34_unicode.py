#file: p34_unicode.py
#desc: 아스키, 유니코드 설명

import sys

a = 'Life is short, you need python'
print(a)
print(type(a))
print(f'a 바이트 크기: {sys.getsizeof(a)}')

b = a.encode('utf-8')   #유니코드로 변환
print(b)
print(type(b))  #<class 'bytes'>, 2진수로 데이터 표현, 네트워크로 데이터 전송/DB에 저장/파일로 저장 등 데이터 전송에 최적화
print(f'b 바이트 크기: {sys.getsizeof(b)}')

c = a.encode('euc-kr')   #or cp949  #한글 체계 cp949로 변환
print(c)    #<class 'bytes'>
print(type(c))  
print(f'c 바이트 크기: {sys.getsizeof(c)}')

print(b.decode('utf-8'))    #유니코드로 문자열 변환
