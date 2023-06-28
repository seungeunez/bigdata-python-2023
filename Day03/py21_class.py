# 클래스 예제
import sys

class Calculator:
    def __init__(self) -> None:
        self.result = 0 # 밖에서 result = 0 선언하는거랑 똑같음
    
    def add(self, num):
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result
    
    def mul(self, num):
        pass
        
    
mycalc = Calculator() # java와 달리 new 없음
print(mycalc.add(40))
print(mycalc.add(50))