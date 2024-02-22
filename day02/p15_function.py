#file: p15_function.py
#desc: 함수 학습

#사용자 정의 함수
def plus(a, b):     #매개변수, 리턴값 존재
    res = a + b
    return res

def minus(a, b):    #매개변수만 있음
    res = a - b
    print(res)

def multi():    #리턴값만 있음
    global a, c     #전역변수 a, c 사용
    res = a * c
    return res

def divide():   #매개변수, 리턴값 모두 없음
    global a, c
    print(a / c)

def pow(a, b = 10):     #기본 인수 지정 시 뒤에서 부터 해야 함
    res = a ** b
    return res

print('더하기')
a = 10
c = 7
print(plus(a, c))

minus(a, c)

print(multi())
divide()

print(pow(2))

def plus_many(*nums):   # *: 매개변수 여러 개 받을 수 있음(가변 매개변수)
    sum = 0
    for i in nums:
        sum += i
    return sum

print(plus_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))    

def calculator(mode, *args):    #동적 매개변수 / 가변 매개변수
    if mode == 'a':
        result = 0
        for i in args:
            result += i
    elif mode == 'n':
        result = args[0]
        for i in args[1:]:
            result -= i
    elif mode == 'm':
        result = 1
        for i in args:
            result *= i
    elif mode == 'd':
        result = args[0]
        for i in args[1:]:
            result /= i
    return result

print(calculator('a', 1, 2, 3, 4, 5))   #15
print(calculator('n', 100, 10, 5, 5, 4))    #76
print(calculator('m', 2, 2, 2, 2, 2))   #32
print(calculator('d', 100, 5, 4, 5))    #1.0


def print_kwargs(**items):  #키워드 매개변수, 딕셔너리 생성함
    print(items)

print_kwargs(name = 'Peter Parker', age = 18, weapon = 'wep shooter')

def calc2(a, b):
    res1 = a + b
    res2 = a - b
    res3 = a * b
    res4 = a / b

    return (res1, res2, res3, res4)     #2개 이상 리턴 가능(튜플로 리턴됨)

a, b, c, d = calc2(4, 2) 
print(a, b, c, d)


#익명 함수(람다 함수)
add = lambda a, b: a + b    #한번 쓰고 말 간단한 함수 작성 시 사용
print(add(4, 5))

