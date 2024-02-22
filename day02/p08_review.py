#file: p08_review.py
#desc: 되새김 문제(2장)

#Q1. 평균 점수 구하기
result = (80 + 75 + 55) / 3
print(result)

#Q2. 홀수, 짝수 판별
a = 13
if a % 2 == 0:
    print('짝수')
else:
    print('홀수')

#Q3. 주민등록번호 나누기
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)
#or
yyyymmdd = pin.split("-")[0]
num = pin.split("-")[1]
print(yyyymmdd)
print(num)

#Q3-1. 주민등록번호 생년월일
pin = "881120-1068234"
if pin[7] == "1" or pin[7] == "2":
    yyyymmdd = '19' + pin[:6]
elif pin[7] =="3" or pin[7] == "4":
    yyyymmdd = '20' + pin[:6]
print(yyyymmdd)
 
#Q4. 주민등록번호 인덱싱
pin = "881120-1068234"
print(pin[7])

#Q5. 문자열 바꾸기
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

#Q6. 리스트 역순 정렬하기
a = [1, 3, 5, 4, 2]
a.sort()    #오름차순 정렬
a.sort(reverse=True)    #내림차순 정렬
print(a)

#Q7. 리스트를 문자열로 만들기
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

#Q8. 튜플 더하기
a = (1, 2, 3)
a += (4, )
print(a)

#Q10. 딕셔너리 값 추출하기
a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)
print(result)

#Q11. 리스트에서 중복 제거하기
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)
