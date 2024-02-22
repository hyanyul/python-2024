#file: p11_whileCondition
#desc: while 반복문

hit = 0

while hit < 50:     #True인 동안 계속 반복됨, False가 되는 순간 while문 빠져나감
    hit += 1
    if hit % 3 == 0:
        #print("호우!")
        continue    #반복문의 아래로 내려가지 말고 위로 올라감 / 반복문에서만 사용 가능
    else:
        print(f'나무를 {hit:02d}번 찍었습니다.')
    if hit == 10:
        print("나무가 넘어갑니다.")
        break   #조건에 상관없이 반복문 탈출 / 반복문에서만 사용 가능

#무한 루프
#hit = 0
#while True:
#   hit += 1
#   print(f'나무를 {hit:02d}번 찍었습니다.')

import os

while True:
    os.system('cls')
    select = input('메뉴 선택  1. 입력  2. 수정  3. 검색  4. 삭제  5. 종료 > ')
    
    if select == '1':
        print('데이터 입력')
        input()
    elif select == '2':
        print('데이터 수정')
        input()

    elif select == '3':
        print('데이터 검색')
        input()

    elif select == '4':
        print('데이터 삭제')
        input()

    elif select == '5':
        print('종료')
        break
    else:
        print('입력 오류')
        continue
