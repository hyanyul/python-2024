#file: p10_forCondition.py
#desc: for 반복문

#문법-for item in 반복할객체:
#       수행할 문장1

#a = 1
#for i in a:     #정수형 못넣음
#    print(i)    

a = [1, 2, 3]
for i in a:
    print(i)

for i in [1, 3, 5, 7, 9]:
    print(i)

print(type(a))  #<class 'list'>

for i in [1, 3, 5, 7, 9]:
    print(type(i))  #<class 'int'>

for i in ['one', 'two', 'three']:
    print(type(i))  #<class 'str'>

b = [(1, 2), (3, 4), (5, 6)]    #튜플의 리스트
for i in b:
    print(type(i))  #<class 'tuple'>
    
for (first, second) in b:
    print(first, second)    #각 튜플이 분해돼서 출력됨

for first, second in b:     #튜플 소괄호 생략 가능(위 for문과 같은 결과 나옴)
    print(first, second)


#평균 내기
grade = [90, 80, 50, 70, 10]
sum = 0
for i in grade:
    sum += i

print(sum)    #총합
print(sum / len(grade))    #평균


#range()
print(range(10))    #range(0, 10)을 생략형으로 작성한 것
print(range(0, 10))

for i in range(10):     #range(0, 10) == 0~9
    print(i, end = ",")
print()
print(list(range(0, 10)))

print(list(range(0, 10, 2)))    #0~9에서 2단위로 출력(0, 짝수 출력)
print(list(range(1, 10, 2)))    #0~9에서 2단위로 출력(홀수 출력)

print(list(range(10, 0, -2)))   #10~1까지 -2단위로 출력
print(list(range(4, 101, 4)))   #4의 배수 출력
print(list(range(10, 0, -1)))   

res = 0
for i in range(1, 11):
    res += i

print(res)


#list comprehension(리스트 내포)
#list(range()) 만으로도 list 생성 가능하지만 여러 조건으로 리스트 생성 시 리스트 내포 사용이 좋음
print([i for i in range(1, 1001)])  #복잡한 리스트 만들 때 사용
print(list(range(1,1001)))

print([num * 3 for num in range(1, 1001) if num % 3 == 0])  #3의 배수에 3 곱해서 리스트 만듦

