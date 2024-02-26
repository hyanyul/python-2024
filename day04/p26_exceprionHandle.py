#file: p26_exceptionHandle.py
#desc: 예외처리

#오류(Error): 코드 상 빨간색/노란색 밑줄 그어지는 것, 문법적으로 문제 있음
#예외(Exception): 문법적으론 문제가 없으나 프로그램 실행 중에 생기는 오류(비정상적으로 종료됨)

#f = open('./sanple.txt', mode='r', encoding='utf-8')    #파일 이름 잘못 적는 실수
#f.close()

#print(5 / 0)    #0으로 나누기 불가

a, b = 5, 3

#if a > b    #콜론 없음
#    print(True)

#if a = b:   #비교연산자를 사용해야 하는데 대입연산자를 사용함
#    print(True)

#1. 파일 읽기
try: 
    f = open('./sanple.txt', mode='r', encoding='utf-8')    #예외로 인해 프로그램 진행이 안됨
    res = f.readline()
    print(res)
except:
    print("파일 오픈 예외 발생")
else:
    f.close()   #예외 발생 없을 때 사용
# finally:
#     try:
#         f.close()   #예외가 발생하든 안하든 무조건 파일 닫아줌
#     except NameError as e:
#         print("파일 오픈 실패")

#2. 계산결과
try:
    print(5 / 0)
except:
    print("[예외발생] 0으로 나눌 수 없습니다.")


