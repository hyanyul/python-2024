#file: p16_io.py
#desc: 입출력 학습

#input() 함수 기본
#res = input('인사말을 적으세요 > ')
#print(res)

#num = input("곱할 수를 적으세요 > ")
#print(num)
#print(type(num))    #<class 'str'> / input()로 받는 모든 값은 문자열임
#print(num * 2)  #34 입력 시 3434 나옴(문자열로 인식돼서 곱한만큼 반복됨)


#num = int(num)      #int로 형변환
#print(type(num))    #<class 'int'>
#print(num * 2)      #숫자로 인식돼서 곱하면 2배 수 나옴

# num = int(input('2로 곱할 숫자 입력 >>> '))     #정수 외의 값 입력 시 예외 뜸
# print(num * 2)

#여러값 입력
int(40.2)   #40
int('50')   #50
# int('40.2')    #불가
# int((10, 20, 30))   #튜플 바로 int로 변환 불가


# 튜플의 괄호 중 할당을 받는 쪽의 괄호()는 생략 가능
# (a1, a2, a3) = input('합산할 세 개의 값 입력(구분자 space) > ').split(' ')   #입력값 -> 튜플됨 == int로 변환 불가
# print(a1)
# print(a2)
# print(a3)
# a1 = int(a1)    #하나씩 변환해야 함
# a2 = int(a2)
# a3 = int(a3)
# sum = a1 + a2 + a3
# print(f'합계는 {sum}')

a1, a2, a3 = map(int, input('합산할 세 개의 값 입력(구분자 space) > ').split(' '))  #값 입력 한 번에 하고, int로 바꿀 수 있음
print(f'합계: {a1 + a2 + a3}')
