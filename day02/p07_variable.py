#file: p07_variable.py
#desc: 변수에 대하여
from copy import copy

z = 1
print(id(z))    #메모리 주소 리턴

a = [1, 2, 3]   #주소값 계속 달라짐 / 작업 다시 실행 시 메모리 다시 할당됨. 스택은 변동폭 좁음, 힙은 변동폭이 커서 크게 바뀜
print(id(a))

b = a
print(id(b))

c = 1
d = c
print(id(c))
print(id(d))

#del b[2]
#print(a)    #a, b는 같은 객체를 가리키기 때문에 b를 수정하면 a도 수정됨

b = copy(a)
print(id(b))
del b[2]
print(a)
print(b)
