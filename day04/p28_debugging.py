#file: p28_debugging.py
#desc: 디버깅 학습, 예외처리 추가

class newCalc:
    def add(self, a, b):
        res = a + b
        return res
    
    def minus(self, a, b):
        res = a - b
        return res
    
    def mul(self, a, b):
        res = a * b
        return res
    
    def div(self, a, b):
        res = a / b
        return res
    
while True:
    try:
        select = int(input('메뉴  1. 더하기, 2. 빼기, 3. 곱하기, 4. 나누기, 5. 종료 > '))
    except:
        print('1~5까지의 숫자만 입력하세요.')
        continue

    if select == 1:     #중단점: 멈추는 부분
        try: 
            x, y = map(int, input('두 수 입력(정수) > ').split())
        except:
            print('정수만 입력해주세요.')
            input()
            continue
        calc = newCalc()
        print(f'더하기 결과: {x} + {y} = {calc.add(x, y)}')
    elif select == 2:
        try: 
            x, y = map(int, input('두 수 입력(정수) > ').split())
        except:
            print('정수만 입력해주세요.')
            input()
            continue
        calc = newCalc()
        print(f'빼기 결과: {x} - {y} = {calc.minus(x, y)}')
    elif select == 3:
        try: 
            x, y = map(int, input('두 수 입력(정수) > ').split())
        except:
            print('정수만 입력해주세요.')
            input()
            continue
        calc = newCalc()
        print(f'빼기 결과: {x} × {y} = {calc.mul(x, y)}')
    elif select == 4:
        try: 
            x, y = map(int, input('두 수 입력(정수) > ').split())
        except:
            print('정수만 입력해주세요.')
            input()
            continue
        if y == 0:
            print("제수에 0을 입력하지 마세요.")
            continue
        calc = newCalc()
        print(f'빼기 결과: {x} ÷ {y} = {calc.div(x, y)}')
    elif select == 5:
        print('프로그램 종료')
        input()    #임시로 멈춤(입력하면 끝나게 됨)
        break
    else:   #1~5 외의 입력이 들어오면
        print('1~5까지의 메뉴 중에서 입력해주세요.')
        continue
    
