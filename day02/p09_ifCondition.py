#py09_ifCondition.py
#desc: if 제어문

haveMoney = True
if haveMoney:
    #indentation(들여쓰기) tab == space * 4(설정에서 변경 가능)
    print('택시를 타고 가')
    print('부럽네')    #들여쓰기로 수행할 문장을 판단하기 때문에 들여쓰기 철저히 줄 맞춰줘야 함
else:
    print('걸어가!')
    print('돈 없어')


money = 1000
if money >= 5000:
    print('택시를 타고 가')
    print('부럽네') 
elif money < 5000 and money >= 2500:
    print('기사님 홈플러스 앞까지만 가주세요')
    print('집까지 걸어가요')
else:
    print('걸어가!')
    print('돈 없어')


a, b, c, d = 10, 5, 7, 9

print(a >= b)   #Ture
print(c > d)    #False

print(a >= b and c > d) #False  and: 둘 다 참일 때 True
print(a >= d or c > d)  #True   or: 둘 중 하나만 참이어도 True / 둘 다 거짓일 때만 False

print(not (a >= b)) #False  not: 참/거짓을 반대로 리턴

#print(): end 옵션(많이 씀), sep 옵션
print(1 in [1, 3, 5, 7, 9], end = ', ')   #리스트 안에 1이 있는가 True  end: 개행 대신 뭘로 할지 설정 가능
print(6 in [1, 3, 5, 7, 9])    #False

print('13579', '246810', sep=".")   #sep: 구분자 설정 가능

#조건 연산자 / 파이썬에선 잘 안씀
score = 60
print('sucess' if score >= 60 else 'falure')    #자바 삼항 연산자와 동일
