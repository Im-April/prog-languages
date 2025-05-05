# # 마린 : 공격 유닛, 군인, 총을 쏜다
# name = '마린' # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격

# print(f'{name}유닛이 생성되었습니다')
# print(f'체력 : {hp}\t유닛의 공격력 : {damage}')

# # 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반모드 / 시즈모드.
# tank_name='탱크'
# tank_hp=150
# tank_damage=35

# print(f'{tank_name} 유닛이 생성되었습니다.')
# print(f'체력 : {tank_hp}\t유닛의 공격력 : {tank_damage}')

# tank2_name='탱크2'
# tank2_hp=140
# tank2_damage=25

# print(f'{tank2_name} 유닛이 생성되었습니다.')
# print(f'체력 : {tank2_hp}\t유닛의 공격력 : {tank2_damage}')

# def attack(name, location, damage):
# 	print(f'{name}유닛이 {location} 방향으로 {damage}만큼의 공격을 합니다')

# attack(name,'1시',damage)
# attack(tank_name,'1시',tank_damage)
# attack(tank2_name,'1시',tank2_damage)


# 클래스 사용
# 하나의 틀

class Unit:
	def __init__(self, name, hp,damage):
		self.name = name
		self.hp = hp
		self.damage = damage
		print(f'{self.name} 유닛이 생성되었습니다.')
		print(f'체력 {self.hp}\t공격력 : {self.damage}')

marine1 = Unit('마린',40,5)
marine2 = Unit('마린',45,4)
tank = Unit('탱크',150,35)