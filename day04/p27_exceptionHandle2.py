#file: p27_exceptionHandle2.py
#desc: 예외처리 2

# while True:
#     try:
#         select = int(input("메뉴 입력  1. 저장, 2. 검색, 3. 종료 > "))
    
#     except ValueError as e:
#         print("[예외발생] 다시 입력해주세요.")
#         continue

#     if select == 1:
#         print('저장')
#     elif select == 2:
#         print('검색')
#     elif select == 3:
#         print('종료')
#         break
#     else:
#         print("메뉴 1~3 중 하나를 선택해주세요.")

class Chiken:
    def fly(self): 
        raise NotImplementedError
  
koko = Chiken()

try: 
    koko.fly()
except Exception as e:
    print("닭은 못날아요..", e.args)    #NotImplementedError는 추가 예외 메시지()가 없음