# #11-9.퀴즈10
# import byme
# byme.sign()

# #11-8.외장 함수
# import datetime
# today = datetime.date.today()
# td = datetime.timedelta(days=100)
# print("우리가 만난지 100일은", today + td)

# import datetime
# print("오늘 날짜는", datetime.date.today())

# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import os # 운영체제에서 제공하는 기본 기능
# print(os.getcwd())

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir)

# import glob # 경로 내의 폴더/파일 목록 조회(윈도우 dir)
# print(glob.glob("*.py"))

# #11-7.내장 함수
# name = "Jim"
# print(dir(name))

# lst = [1, 2, 3]
# print(dir(lst))

# print(dir())
# import random
# print(dir(random))

# language = input("무슨 언어를 좋아하세요?") #사용자 입력을 받는 함수
# print("{0}은 아주 좋은 언어입니다!".format(language))

# #11-6.pip install
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# #11-5.패키지, 모듈 위치
# from travel import *
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

# #11-4.모듈 직접 실행
# from travel import *
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# #11-3.__all__
# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# #11-2.패키지
# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from travel.thailand import ThailandPaackage # from 구문에선 가능
# trip_to = ThailandPaackage()
# trip_to.detail()

# import travel.thailand #import로 시작되는 함수는 class(ThailandPackage)를 바로 적용할 수 없다.
# trip_to = travel.thailand.ThailandPaackage() # 모듈(travel).패키지(thailand).클래스(ThailandPackage)
# trip_to.detail()

# #11-1.모듈
# from theater_module import price_soldier as price
# price(5)

# from theater_module import price, price_morning
# price(5)
# price_morning(6)
# #price_soldier(7) # 사용불가

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# #10-5.퀴즈9
# class SoldOutError(Exception):
#     pass

# chicken = 10
# waiting = 1
# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken:
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1
#             chicken -= order

#         if chicken == 0:
#             raise SoldOutError        
#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break

# #10-4.finally
# class BigNumberError(Exception):
#     # pass
#     def __init__(self, msg):
#         self.msg = msg
    
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >=10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")

# #10-3.사용자 정의 예외처리
# class BigNumberError(Exception):
#     # pass
#     def __init__(self, msg):
#         self.msg = msg
    
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >=10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)

# #10-2.에러 발생시키기
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >=10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

# #10-1.예외처리
# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)

# #9-12.퀴즈8
# class House:
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

# houses = []
# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# house3 = House("송파", "빌라", "월세", "500/50", "2000년")

# houses.append(house1)
# houses.append(house2)
# houses.append(house3)

# print("총 {0}대의 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     house.show_detail()

# #9-10~11.스타크래프트 프로젝트 전반전/후반전
# from random import *

# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다".format(name))
    
#     def move(self, location):
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
        
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)

#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# class Tank(AttackUnit):
#     seize_developed = False

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return

#         if self.seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *=2
#             self.seize_mode = True
#         else:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /=2

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0 ,damage)  # 지상 Speed 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         self.fly(self.name, location)

# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False

#     def clocking(self):
#         if self.clocked == True:
#             print("{0} : 클로킹 모드 해제합니다.".format(self.name))
#             self.clocked = False
#         else:
#             print("{0} : 클로킹 모드 설정합니다.".format(self.name))
#             self.clocked = True

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print("Player : gg")
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")


# game_start()

# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# t1 = Tank()
# t2 = Tank()

# w1 = Wraith()

# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# for unit in attack_units:
#     unit.move("1시")

# Tank.seize_developed = True
# print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# for unit in attack_units:
#     unit.attack("1시")

# for unit in attack_units:
#     unit.damaged(randint(5, 20))

# game_over()

# #9-9.super
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
    
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0 ,damage)  # 지상 Speed 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)
#         self.location = location

# #9-8.pass
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
    
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0 ,damage)  # 지상 Speed 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass

# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()


# #9-7.메소드 오버라이딩
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
    
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0 ,damage)  # 지상 Speed 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# vulture = AttackUnit("벌쳐", 80, 10, 20)
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")

# #9-6.다중 상속
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# class FlayableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)

# valkyrie = FlayableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# #9-5.상속
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

# #9-4.메소드
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))
            
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

# #9-3.멤버 변수
# class 내에서 정의된 변수
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage ))

# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# #9-2.__init__
# 객체가 만들어질 때 생성자
# class 로부터 만들어지는 것 == 객체
# marine, tank 같은 것은 Unit class의 인스턴스라고 함

# #9-1.클래스
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# name = "마린"
# hp = 40
# damage = 5

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# tank_name = "탱크"
# tank_hp = 150
# tank_damage =35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage =35

# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# #퀴즈7
# for i in range(1, 51):
#     with open(str(i) + "주차.txt", "w", encoding=("utf8")) as report_file:
#         report_file.write("- {0}주차 주간보고 -".format(i))
#         report_file.write("\n부서 : ")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무 요약 : ")

# #8-5.with  #pickle과 유사하지만 파일을 close할 필요가 없다
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# #8-4.pickle
# import pickle
# profile_file = open("profile.pickle", "rb") #"rb"==읽기 바이너리(피클을 사용하기위해선 b바이너리가 필요)
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# import pickle
# profile_file = open("profile.pickle", "wb") #"wb"==쓰기 바이너리(피클을 사용하기위해선 b바이너리가 필요)
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile 에 있는 정보를 file에 저장
# profile_file.close()

# #8-3.파일입출력
# score_file = open("score.txt", "r", encoding="utf8") #"r"==읽기
# lines = score_file.readlines() #list 형태로 저장
# for line in lines:
#     print(line, end="")

# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") #"r"==읽기
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") #"r"==읽기
# print(score_file.readline(), end="") # 줄별로 읽기, 커서는 다음줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") #"r"==읽기
# print(score_file.readline()) # 줄별로 읽기, 커서는 다음줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") #"r"==읽기
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") #"a"==추가
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "w", encoding="utf8") #"w"==쓰기
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# #8-2.다양한 출력 포맷
# print("{0: >10}".format(500))

# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))

# print("{0:_<+10}".format(500))

# print("{0:,}".format(10000000000))

# print("{0:+,}".format(10000000000))

# print("{0:^<+30,}".format(10000000000))

# print("{0:f}".format(5/3)) #소수점
# print("{0:.2f}".format(5/3))

# #8-1.표준입출력
# answer = input("아무 값이나 입력하세요 : ") #input으로 입력된 값은 str형태로만 적용
# print("입력하신 값은 " + answer + "입니다.")

# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     #print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# print("Python", "Java", sep=", ", end="?")
# print("무엇이 더 재밌을까요?")

# #퀴즈6
# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 175
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {0}cm, {1}의 표준 체중은  {2}kg 입니다.".format(height, gender, weight))

# #7-6.지역변수와 전역변수
# gun = 10

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

# gun = 10

# def checkpoint(soldiers):
#     global gun #전역공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))

# #7-5.가변인자
# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print() #줄바꿈용

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
# profile("김태호", 25, "Kotlin", "Swift")

# def profile(name, age, lang1, lang2, lang3, lang4,lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")


# #7-4.키워드값
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")

# #7-3.기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\n나이 : {1}\n주 사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\n나이 : {1}\n주 사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# #7-2.전달값과 반환값
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money): #입금
#     print("입급이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money): #출금
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 안료되지 않았습니다. 잔액은 {0} 원 입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# balance = 0
# balance = deposit(balance, 1000)
# #balance = withdraw(balance, 500)
# #balance = withdraw(balance, 2000)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0} 원 이며, 잔액은 {1} 원 입니다.".format(commission, balance))

# #7-1.함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()

# #퀴즈5
# from random import *
# cnt = 0
# for i in range(1, 51):
#     time = randrange(5, 51)
#     if 5 <= time <= 15:
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

# print("총 탑승 승객 : {0}분".format(cnt))

# #6-5.한줄 for
# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

# #6-4.continue와 break
# absent = [2, 5]
# no_book = [7]
# for student in range(1, 10):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0} 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

#6-3.while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1
#     if index ==0:
#         print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
#     index += 1
    
# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")    

# #6-2.for
# for waiting_no in [0, 1, 2, 3, 4]:
#     print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(5):
#     print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(1, 6):
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# #6-1.if
# weather = input("오늘 날씨는 어때요? : ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

# #퀴즈4
# from random import *
# users = range(1, 21)
# users = list(users)
# shuffle(users)

# winners = sample(users, 4)
# print(" -- 당첨자 발표 -- ")
# print(" 치킨 당첨자 :  {0} ".format(winners[0]))
# print(" 커피 당첨자 :  {0} ".format(winners[1:]))
# print(" -- 축하합니다!! -- ")

# #5-5.자료구조의 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# # 5-4.세트 #중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])
# print(java & python) # 교집합
# print(java.intersection(python)) # 교집합

# print(java | python) # 합집합
# print(java.union(python)) # 합집합

# print(java - python)
# print(java.difference(python))

# python.add("김태호")
# print(python)

# java.remove("김태호")
# print(java)

# #5-3.튜플 # 리스트와 유사하게 사용하지만 변경이 불가능
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# name = "김종국"
# age =  20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

# #5-2.사전
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet[5])
# print(cabinet.get(5))
# print(cabinet.get(5, "사용 가능"))
# print("hi")

# print(3 in cabinet)
# print(5 in cabinet)

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# del cabinet["A-3"]
# print(cabinet)

# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items())

# cabinet.clear()
# print(cabinet)

# #5-1.리스트
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# print(subway.index("조세호"))

# subway.append("하하")
# print(subway)

# subway.insert(1, "정형돈")
# print(subway)

# print(subway.pop())
# print(subway)

# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# num_list = [5, 4, 3, 2, 1]
# num_list.sort()
# print(num_list)

# num_list.reverse()
# print(num_list)

# num_list.clear()
# # print(num_list)

# num_list = [5, 4, 3, 2, 1]
# mix_list = ["조세호", 20, True]
# print(mix_list)

# num_list.extend(mix_list)
# print(num_list)

# #퀴즈3
# url = "https://nnspwork.co.kr"
# my_str = url.replace("https://", "")

# print("사이트 : " +  url)
# print("첫번째 규칙 적용 " +  my_str)
# my_str = my_str[:my_str.index(".")]
# print("두번째 규칙 적용 " +  my_str)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

#4-5.탈출문자
# print("백문이 불여일견\n백견이 불여일타") # \n : 줄바꿈
# print("저는 \"나도코딩\"입니다.") # \" \' : 문장내에서 따옴표 쓰기
# \\ : 문장내에서 \ 쓰기
# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")
# \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")
# \t : 탭
# print("Red\tApple")

#4-4.문자열 포맷
# print("a" + "b")
# print("a", "b")

# print("나는 %d살입니다." % 20) # 정수
# print("나는 %s을 좋아해요." % "파이썬") # 문자
# print("Apple 은 %c로 시작해요." % "A") # 한글자
# %s를 쓰면 출력 다 됨
# # print("나는 %s색과 %s색을 좋아해요." % ("파란","빨간"))
# print("나는 {}살 입니다.".format(20))
# print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))

# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age = 20))

# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# #4-3.문자열처리함수
# python = "Python is Amazing"
# print(python.lower()) # 전체 소문자
# print(python.upper()) # 전체 대문자
# print(python[0].isupper()) # 특정 위치의 값이 대문자인지 확인
# print(len(python)) # 길이값
# print(python.replace("Python", "Java")) #특정 단어 변환

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)

# print(python.find("n"))

# print(python.find("Java"))
# # print(python.index("Java"))

# print(python.count("n"))

# #4-2.슬라이싱
# jumin = "990120-1234567"
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2])
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])

# print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
# print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

#4-1.문자열
# sentence = '나는 소년입니다.'
# print(sentence)
# sentence2 = "파이썬은 쉬워요."
# print(sentence)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요.
# """
# print(sentence3)

# #퀴즈2
# from random import *
# date = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")

#3-4.랜덤함수
# from random import * 
# print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random() * 10)
# print(int(random()* 10))
# print(int(random()* 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

#로또번호
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)

# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))
# print(randrange(1, 46))

# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45))
# print(randint(1, 45))
# print(randint(1, 45))
# print(randint(1, 45))
# print(randint(1, 45))

# #3-3.숫자처리함수
# print(abs(-5)) # 절대값
# print(pow(4, 2)) # 제곱
# print(max(5, 12)) # 최대값
# print(min(5, 12)) # 최소값
# print(round(3.14)) # 반올림
# print(round(4.99)) # 반올림

# from math import *
# print(floor(4.99)) # 내림
# print(ceil(3.14)) # 올림
# print(sqrt(16)) # 제곱근

# #3-2.수식
# print(2 + 3 * 4)
# print((2 + 3)* 4)
# number = 2 + 3 * 4
# print(number)
# number = number + 2
# print(number)
# number += 2
# print(number)
# number *= 2
# print(number)
# number /= 2
# print(number)
# number -= 2
# print(number)

# number %= 5
# print(number)

# #3-1.연산자
# print(1+1)
# print(3-2)
# print(5*2)
# print(6/3)

# print(2**3)
# print(5%3) # 나머지
# print(10%3)
# print(5//3) # 몫

# print(10 > 3)
# print(4 >= 7)
# print(10 < 3)
# print(5 <= 5)

# print(3 == 3)
# print(4 == 2)
# print(3 + 4 == 7)

# print(1 != 3)
# print(not(1 !=3))

# print((3 > 0 ) and (3 < 5))
# print((3 > 0 ) & (3 < 5))

# print((3 > 0) or (3 > 5))
# print((3 > 0) | (3 > 5))

# print(5 > 4 > 3)
# print(5 > 4 > 7)

#퀴즈1
# station = "사당"
# print(station + "행 열차가 들어오고 있습니다.")

#2-5.주석
# 범위지정 후 컨트롤 + / 

#2-4.변수
# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = age >= 3

# print("우리집 " + animal + "의 이름은 " + name + "예요")
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name + "는 어른일까요? " + str(is_adult))

#2-3.불리안 자료형(참/거짓)
#print(5>10)
#print(5<10)
#print(True)
#print(False)
#print(not True)
#print(not False)
#print(not (5 > 10))

#2-2.문자열 자료형
#print('풍선')
#print("나비")
#print('ㅋㅋㅋㅋㅋㅋ')
#print('ㅋ'*6)

#2-1.숫자형 자료형
#print(5)
#print(-10)
#print(3.14)
#print(1000)
#print(5+3)
#print(2*8)
#print(3*(3+1))


