#file: p06_bool.py
#desc: 불 타입, None 타입 학습

#참/거짓
a = True
b = False

print(a)
print(type(b))  #<class 'bool'>
print(type(1))  #<class 'int'>
print(type(3.14))   #<class 'float>
print(type('Hi'))   #<class 'str'>
print(type([1,2,3]))    #<class 'list'>
print(type((1,2,3)))    #<class 'tuple'>

print(a == b)
print(a == (not b))

#값이 들어있지 않거나(빈값) 0, None일 경우 거짓으로 판별됨
print(bool(0))  #0은 거짓
print(bool(3))  #0 이외의 값은 참


#None 타입
c = None
#a = 1
#b = 0

print(c)
print(a + b)    #a: True, b: False
#print(c + a)   #None값은 연산 불가

c = 3
print(c + a)


