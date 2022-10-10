class Unit:
    def __init__(self):
        print("Unit 생성자")
        
class Flyable:
    def __init__(self):
        print("Flyable 생성자")
        
class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__() 순서상으로 먼저 적힌 class만 실행됨
        Unit.__init__(self)
        Flyable.__init__(self)
        
# 드랍쉽
dropship = FlyableUnit()
