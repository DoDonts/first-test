class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()  #super를 이용해 다중상속을 받을때는 맨 처음 상속받는 class 만 호출됨
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()