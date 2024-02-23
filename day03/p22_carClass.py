#file: p22_carClass.py
#desc: 객체 지향 클래스 학습

class Car:
    __carNum = ''   #__: 접근 제한자==private, 그냥 쓰면 public
    company = ''
    releaseYear = 1960
    color = '흰색'
    carType = ''
    fuelType = '가솔린'

    def __init__(self, carNum) -> None:    #생성자  #None: 리턴 없음 / 생성자는 리턴값 없음     #매직 메서드
        self.__carNum = carNum
        print(f'{self.__carNum} 객체를 생성합니다.')

    def __str__(self) -> str:   #객체 변수를 print() 할 때 출력 커스터마이징 함수
        return f'내 차는 {self.company}, {self.__carNum} 입니다.'

    def setCarNum(self, carNum) -> None:
        self.__carNum = carNum
    
    def getCarNum(self) -> str:
        return self.__carNum

    def getColor(self):
        print(f'{self.__carNum}은(는) {self.color} 입니다.')

    def start(self):    #self: 지역 변수를 사용하기 위해 필요
        print(f'{self.__carNum}이(가) 시동을 겁니다.')

    def accel(self):
        print(f'{self.__carNum}엑셀을 밟습니다.')
    
    def brake(self):
        print(f'{self.__carNum}이(가) 브레이크를 밟습니다.')
    
    def turnLeft(self):
        print(f'{self.__carNum}이(가) 좌회전 합니다.')

    def turnRight(self):
        print(f'{self.__carNum}이(가) 우회전 합니다.')