#file: p25_usingModule.py
#desc: 모듈 사용


import calc  as c   #calc.py 가져와서 사용 가능
from calc import mul   #mul() 함수명만 쓰면 됨, 여러 개의 모듈 사용 시 충돌남(함수명 같은 경우) - as 통해서 이름 바꿔 쓰면 충돌 방지 가능

#import Math
#from Math import Math #from Math: 모듈(파일 이름), import Math: 클래스 이름

from day03.p22_carClass import Car  #디렉토리: 모듈 묶음(패키지). 모듈명

if __name__ == '__main__':  #java의 void main과 동일
    res = c.mul(10, 7)      #원래 calc로 접근해서 사용해야 하지만 import 시 as c를 붙여줌으로써 c로 접근 가능
    print(res)

    print(__name__)     #__main__ : 본인이 가시적으로 폴더 안에서 시작되는 포인트(메인 엔트리)라고 알리고 싶을 때 사용(옵션)

    #myMath = Math.Math()   #from Math import Math 없으면 이렇게 적어줘야 함
    myMath = Math()
    print(myMath.solv(10))


