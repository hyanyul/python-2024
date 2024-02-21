#file: p01_number.py
#desc: 숫자형 자료 타입 및 연산자


#일반 숫자형
age = 40   #int형 담는 변수
taxRate = 8.8   #float형을 담는 변수
highFloats = 4.24E10   #지수승(float)

print("나이는", age)   #내용 도움자가 자동완성 도와줌
print('세율은', taxRate)   #문자열 "", '' 둘 다 사용 가능
print('지수값은', highFloats)   #문자형 없음, 무조건 다 문자열

#특수 숫자형
binVal = 0b11111111   #255(2진수)  /  0, 1로 표현
octVal = 0o11   #9(8진수)  /  1~7 
hexVal = 0xFF   #255(16진수)  /  0~9ABCDEF

print('2진수:', binVal, '/ 8진수:', octVal, '/ 16진수:', hexVal)

#타입 적을 필요 없음==그냥 쓰면 됨


#사칙연산
a, b, c = 3, 4, 9
print(a + b)
print(a - c)
print(a * c)

#나누기 3가지로 분류
print(c / b)   #정확하게 실수로 나눔
print(c // b)   #정수로만 나눈 몫, 뒤에 버려짐
print(c % b)   #정수로 나눈 나머지 

print(2 ** 10)   #2^10(==1024)  import math; math.pow()

print((a + b) * c)   #연산자 우선순위: 괄호만 잘 치면 됨