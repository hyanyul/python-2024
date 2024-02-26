#file: p29_builtInFunc.py
#desc: 내장함수

#abs(absolute 준말)-절대값
print(abs(-5))

#all-현재 컬렉션 데이터의 조건, 값이 참인 값만 있는지 확인
print(all([1, 2, 3, 4, 0]))

#chr()-아스키나 유니코드 값을 받아서 글자로 변경
print(chr(65))  #A
print(chr(97))  #a
print(chr(44032))   #가

#ascii()-영문자, 문자를 아스키숫자와 유니코드 숫자로 변경
print(ascii('가'))

#dir()-객체가 지닌 변수, 함수를 알려주는 함수
print(dir(list()))
print(dir(dict()))

#divmod()-나누기의 몫, 나머지를 한 번에 구해주는 함수
print(divmod(7, 2))    #(3, 1)-앞이 몫, 뒤가 나머지

#★enumerate()-열거, 데이터 포함 인덱스를 같이 생성해주는 역할
for (i, data) in enumerate(['Hello', 'World', 'Python']):   #데이터 하나가 인덱스와 묶여서 튜플 형태로 출력됨
    print(f"{i}번째 값은 {data}입니다.")

#eval(evaluate)()-실행함수, 문자열로 된 수식, 함수를 실행해주는 역할
print(eval('divmod(10, 3)'))

#hex-10진수를 16진수로
print(hex(255).upper())     #upper: 대문자로 출력

#map()-여러 값을 한꺼번에 같은 조건으로 변경할 때 사용
def tTime(x):
    return x * 2;

print(list(map(tTime, [1, 3, 5, 7, 9])))    #map을 써서 반복 데이터를 tTime()으로 처리
print(list(map(int, [1.0, 2.0, 3.0, 4.6])))     #map을 써서 반복 데이터를 int로 바꿈

#max(), min()
print(max([3, 9, 99]))
print(min([3, 9, 99]))

#oct()-8진수
print(oct(34))

#ord() == ascii()
print(ord('a'))    #97
print(ord('A'))    #65
print(ord('가'))

#round()-반올림
print(round(4.6))
print(round(4.45, 1))

#sum()-반복되는 컬렉션 자료 합 구해줌
print(sum([1, 2, 3, 4, 5]))
print(sum(range(1, 101)))

#tuple()-다른 컬렉션을 튜플 자료형으로 변경
print(tuple([1, 2, 3, 4, 5]))

#type()-변수, 데이터의 타입 리턴
print(type('Hello'))
aa = [1, 2, 3, 4]   #<class 'str'>
print(type(aa))     #<class 'list'>

#zip()-동일한 개수로 데이터를 묶어서 리턴
odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]
even2 = [2, 4, 6]
norm = [1, 2, 3, 4, 5]

total = list(zip(odd, even))
print(total)    #개수가 일치하면 쌍으로 묶어서 출력 / 개수 불일치 시 일치하는 것까지만 출력됨
print(list(zip(odd, even2)))
print(list(zip(odd, even, norm)))   #3개씩 묶음

