#file: p24_ionic.py
#desc: 클래스 상속

from p22_carClass import Car

class Ionic(Car):    #상속, Car 클래스를 상속 받아서 ionic 만듦
    __fuelRate = 0.0    #연비

    def setFuelRate(self, rate):
        self.__fuelRate = rate

    def getFuelRate(self) -> float:
        return self.__fuelRate
    
    def getCarNum(self) -> str:
        return f'제 차의 번호는 {super().getCarNum()}입니다.'

myCar = Ionic('54라 9337')
myCar.company = '기아 자동차'
myCar.setFuelRate(23.5)
print(myCar)
print(f'내 차의 연비는 {myCar.getFuelRate()} km/L 입니다.')
print(myCar.getCarNum())
