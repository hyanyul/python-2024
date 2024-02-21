#file: p03_string.py
#desc: 문자열 자료형과 연산

a = "Hello World"
print(a)

b = 'Hello World'
print(b)

c, d = "Hello, 'Ashley'", 'Hello, \'Ashley\''   #탈출 문자 \n, \t 이외에는 잘 사용하지 않음
print(c)
print(d)

e = 'Hello~\n'\
'I\'m Hugo\n'\
'Nice to meet you'

#문자열 여러줄 쓰고 싶을 때는 """ """ 또는 ''' ''' 안에 작성 / 단, 탭도 그대로 나옴(단점)
f = """
Hello~
I'm Hugo.
Nice to meet you, too
"""
print(e)
print(f)


#문자열 연산: +, *
before = 'I wanna go to '
after = 'Boracai! '
print(before + after)   #문자열 연결 시 + 이용
print(after * 3)   #문자열 n번 반복 원할 시 * 이용


#문자열 길이 구하기
print('글자 길이 =', len(before))
print('한글 글자 길이:', len('안녕하세요'))   #글자 길이: 5글자, 용량: 5 * 8byte


# 문자열 인덱싱, 슬라이싱(중요!)
cP = 'Life is too short, You need Python'  #띄어쓰기도 문자로 침(길이 셀 때 포함)
print(len(cP))

# 문자열 슬라이싱
print(cP[8])
print(cP[17])

#cP[8] = 'd' 문자열은 배열이긴 하나 값 바꿀 수 없음
print(cP[12 : 16 + 1])   #[시작 인덱스 : 끝 인덱스 + 1], 우변 비울 시 끝까지, 좌변 비우면 처음부터

print(ascii('안'), ascii('녕'), ascii('하'), ascii('세'), ascii('요'))   #아스키코드로 변환
print(chr(65), chr(97))

#기존 문자열로 새로운 문자열 만들 때는 슬라이싱하고 다른 문자열로 대체 필수
print(cP[:8], 'long', cP[17:])

print(cP[-1])   #마지막 문자열부터 셀 때는 -1부터 1씩 빼줌

#다른 언어에는 - 슬라이싱 없음
print(cP[-6:])
print(cP[-11:-7])   #-로 슬라이싱 할 때도 뒤에는 1 더해줘야 함


#문자열 포매팅(format string)
#파이썬에서는 %d, %s, %c 등 포맷 스트링용 연산자 사용 빈도 낮음
temp = 21
print('현재 온도는 %d도씨 입니다.' %temp)

temp = 17
print('현재 온도는 %d도씨 입니다.' %temp)

#format 함수로 포매팅(가장 일반적)
print('현재 온도는 {0}도씨 입니다.' .format(temp))

#날짜를 포맷으로 만들 때
month = 2
day = 21
hour = 3
min = 19
print('오늘은 {0:02d}월 {1:02d}일 {2:02d}시 {3:02d}분입니다.' .format(month, day, hour, min))  #{0:02d}: 0을 넣어서 두자리 수 맞춰줌

#숫자 자료형
income = 7_000_000_000  #연매출 700만원
print('올해 매출액은 {0:,d}원' .format(income))  #,d: 숫자 자료형 3자리마다 하나씩 , 찍어줌

PI = 3.1415926536
print('파이는 {0:.2f}' .format(PI))  #10.02f == 소수점(.)까지 다 포함해서 10자리, 소수점 뒤는 2자리
#print('{0:d}' .format(PI))  #실수형은 정수형(d)으로 포매팅 불가

#f 포매팅(3.6(2016) 이후 나온 최신 방식)
name = "홍길동"
age = 30
cont = f"나는 {name}이고, 나이는 {age}세이다"
print(cont)

name = '성명건'
age = 47
print(f"나는 {name:>10}이고, 나이는 {age:03d}세이다")
print(f"나는 {name:<10}이고, 나이는 {age:03.1f}세이다")  #정수는 f포맷 가능, 실수는 d포맷 불가


#문자열 함수
a = "Life is too short, You need Python"

print(a.count('Life'))  #1 나옴, 대소문자 구별함
print(a.count('o'))  #5 나옴
print(a.find('sh'))  #12 나옴, 찾는 것의 시작 인덱스 반환
print(a.index('t'))  #8 나옴, 첫번째 t의 위치 알려줌 -> 찾아서 글자 잘라내거나 할 때 많이 사용(count()로 존재하는지 검사하고 써야 예외 안뜸)
print(','.join('abcde'))  #문자열 끊어서 사이에 , 넣어줌

print(a.lower())
print(a.upper())
print(a.capitalize())  #문장 제일 첫번째 단어만 대문자로 바꾸고 나머지 소문자로 출력

#문자열 정렬(공백)
origin = '          Hi          '
print(f'++{origin}++')
print(f'++{origin.lstrip()}++')  #왼쪽 공백 없앰
print(f'++{origin.rstrip()}++')   #오른쪽 공백 없앰
print(f'++{origin.strip()}++')   #양쪽 공백 다 없앰

print(cP.replace('too', '').replace(' short', 'long'))


#문자열 자르기 -> 리스트로 만듦(파이썬에 배열 없음)
cPWords = cP.split(' ')   #공백을 기준으로 문자열 자름->리스트에 저장
print(cPWords)