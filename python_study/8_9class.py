# # 일반유닛 (부모클래스)
# class Unit:
#     def __init__(self, name, hp, speed): 
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print('지상 유닛 이동')
#         print(f'{self.name} : {location} 방향으로 이동합니다. 속도 :  {self.speed} ')
        

# # 공격유닛 (자식클래스)
# class AttackUnit(Unit): 
#     def __init__(self, name, hp, speed, damage): 
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print(f'{self.name} 유닛이 {location} 방향으로 적군을 {self.damage}만큼 공격합니다.')

#     def damaged(self, damage):
#         print(f'{self.name} 유닛이 {damage}의 데미지를 입었습니다')
#         self.hp -= damage
#         print(f'{self.name}의 현재 체력은 {self.hp} 입니다')
#         if self.hp <= 0:
#             print(f'{self.name}은 파괴되었습니다')


# # 날 수 있는 기능
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print(f'{name} : {location} 방향으로 날아갑니다. 속도 : {self.flying_speed}')


# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, speed=0, damage=damage)
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):  # 들여쓰기 수정
#         print('공중 유닛 이동')
#         self.fly(self.name, location)

# # 건물
# class BuildingUnit(Unit):
# 	def __init__(self,name,hp,location):
# 		# Unit.__init__(self, name, hp, 0):
# 		super().__init__( name, hp, 0) # self 없이 사용한다.
# 		self.location = location
          
class Unit:
	def __init__(self):
		print('Unit 생성자')

class Flyable:
	def __init__(self):
		print('Flyable 생성자')
	
class FlyableUnit(Unit, Flyable):
	def __init__(self):
		super().__init__()
	

# 드랍쉽
dropship = FlyableUnit()

'''
다중 상속을 할 때 super()를 사용하면 순서상 맨처음 클래스에 대해 __init__ 함수가 호출된다
다중 상속을 할 때는 따로 명시적으로 코드를 작성해야한다.
'''