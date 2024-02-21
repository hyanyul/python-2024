#file: p04_list.py
#desc: 리스트, 튜플

#파이썬에는 배열이 없음. 리스트로 대신함

even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]

print(even)
print(even[4])   #길이가 n일 때 마지막 인덱스는 n-1임

even[4] = 20
print(even)   #리스트는 인덱스의 값을 변경할 수 있음(문자열: 값을 못바꿔야 좀 더 정확하기 때문에 변경 불가)

datas = [123, 45.6, True, 'Hello', odd, None]   #타입(형) 지정이 없어서 어떤 자료형이든 다 들어갈 수 있음
print(datas)


#인덱싱, 슬라이싱
print(odd[2])   #인덱스 2번에 있는 5 출력

print(even[0] + odd[0])   #숫자형 자료 + 경우 더해짐

cPWords = ['Life', 'is', 'short']
print(cPWords[0] + cPWords[2])   #문자열 자료 + 경우 연결됨

print(even[1:4])   #4, 6, 8 출력됨


#2차원 리스트
#3행 4열-[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

d2Datas = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(d2Datas)

for i in d2Datas:
    print(i)

dm1Col1 = [1, 2, 3, 4]
dm1Col2 = [5, 6, 7, 8]
dm1Col3 = [9, 10, 11, 12]

print([dm1Col1, dm1Col2, dm1Col3])

#리스트 연산은 문자열 연산과 동일함
print(odd * 2)
print(odd + even)


#값 변경
even[3] = 10
print(even)

del even[2]   #del: 값 삭제
print(even)


#리스트 연산 함수
#append(): 리스트 제일 뒤에 추가
even.append(30)
print(even)

#insert(): 원하는 자리에 값 추가
even.insert(2, 6)   #인덱스 2에 6을 넣겠다
print(even)

#sort(): 정렬
origin = [45, 23, 9, 17, 1, 5, 11, 3, 29, 30]
origin.sort()   #오름차순(Ascending) 정렬
print(origin)
origin.sort(reverse=True)   #내림차순(Descending)
print(origin)

#뒤집기
aa = ['a', 'f', 'e', 'b']
aa.reverse()   #순서 역순으로 뒤집음
print(aa)

print(aa.count('a'))
print(aa.index('e'))

bb = [1, 3, 5, 6, 8, 3, 1]
bb.remove(3)   #중복값이 있어도 맨 앞에 있는 해당 값만 지움
print(bb)
 
print(even.pop())   #pop(): 제일 마지막 값 내보냄
print(even.pop())   #스택의 기능 pop을 구현(append: push 기능 구현(마지막에 값 집어넣음))
print(even)


#튜플
#리스트와 동일, 삭제/편집 불가 -> 한번 만들어지면 끝까지 그대로 사용해야 함
tVal = (1, 3, 5, 7, 9)
