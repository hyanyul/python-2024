#file: p32_review.py
#desc: 되새김 문제 5장

#Q1. 클래스 상속받고 메서드 추가하기1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

#Q2. 클래스 상속받고 메서드 추가하기2
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value >= 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

#Q3. 참과 거짓 예측하기
print(all([1, 2, abs(-3)-3]))   #False
print(chr(ord('a')) == 'a')     #True

#Q4. 음수 제거하기
q = [1, -2, 3, -5, 8, -3]
for i in q:
    if i<0:
        q.remove(i)

print(q)

#Q5. 16진수를 10진수로 변경하기


#Q6. 리스트 항목마다 3 곱하여 리턴하기
def three_time(x):
    return x * 3

print(list(map(three_time, [1, 2, 3, 4])))

#Q7. 최댓값과 최솟값의 합
q = [-8, 2, 7, 5, -3, 5, 0, 1]
# q.sort()
# res = q.index(0) + q.index(len(q) - 1)
# print(res)

max = q.index(0)
min = q.index(0)
for i in q:
    if max < i:
        max = i
    if min > i:
        min = i
print(min + max)

#Q11. 날짜 표시하기
import datetime

curr = datetime.datetime.now()
print(f'{curr.year}/{curr.month:02d}/{curr.day:02d} {curr.hour:02d}:{curr.minute:02d}:{curr.second:02d}')
