#file: p04_list.py
#desc: 리스트

#파이썬에는 배열이 없음. 리스트로 대신함

even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]

print(even)
print(even[4])   #길이가 n일 때 마지막 인덱스는 n-1임

even[4] = 20
print(even)   #리스트는 인덱스의 값을 변경할 수 있음(문자열: 값을 못바꿔야 좀 더 정확하기 때문에 변경 불가)

datas = [123, 45.6, True, 'Hello', odd, None]   #타입(형) 지정이 없어서 어떤 자료형이든 다 들어갈 수 있음
print(datas)
