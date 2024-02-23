#file: p21_review.py
#desc: 되새김 문제(4장)

#Q1. 홀수, 짝수 판별하기
def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False

print(is_odd(31))

#Q2. 모든 입력의 평균값 구하기
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1, 2))
print(avg_numbers(1, 2, 3, 4, 5))

#Q3. 프로그램 오류 수정하기1
input1 = int(input('첫 번째 숫자를 입력하세요: '))
input2 = int(input('두 번째 숫자를 입력하세요: '))

total = input1 + input2
print(f'두 수의 합은 {total}입니다.')

#Q4. 출력 결과가 다른 것
# 1.
print("you" "need" "python")    #youneedpython
# 2.
print("you" + "need" + "python")    #youneedpython
# 3.
print("you", "need", "python")  #you need python
# 4.
print("".join(["you" "need" "python"])) #youneedpython

#Q5. 프로그램 오류 수정하기2
f1 = open('./day03/test2.txt', mode='w', encoding='utf-8')
f1.write("Life is too short")
f1.close()

f1 = open("./day03/test2.txt", mode='r', encoding='utf-8')
print(f1.read())
f1.close()

#Q6. 사용자 입력 저장하기
user_input = input("저장할 내용을 입력하세요: ")
f = open('./day03/test3.txt', mode='a', encoding='utf-8')
f.write(user_input)
f.write('\n')
f.close

#Q7. 파일의 문자열 바꾸기
#Q7-1. read() 사용
f = open('./day03/test.txt', mode='r')
body = f.read()     #read(): 문자열로 리턴, 단 길이 제한 있음(텍스트 길면 문장이 잘려서 나옴)
f.close()

body = body.replace('java', 'python')

f = open('./day03/test.txt', mode='w', encoding='utf-8')
f.write(body)
f.close()

#Q7-2. readlines() 사용
f = open('./day03/test.txt', mode='r', encoding='utf-8')
body = f.readlines()
f.close()

body = [body[0], body[1].replace('java', 'python')]
f = open('./day03/test.txt', mode='w', encoding='utf-8')
f.write(body[0] + body[1])
f.close()
