class Unit:
	def __init__(self, name, hp, damage): 
		# 멤버변수 : 클래스 내에서 선언된 변수
		self.name = name
		self.hp = hp
		self.damage = damage
		print(f'{self.name} 유닛이 생성되었습니다.')
		print(f'체력 {self.hp}\t공격력 : {self.damage}')


class AttackUnit:
	def __init__(self, name, hp, damage): 
		# 멤버변수 : 클래스 내에서 선언된 변수
		self.name = name
		self.hp = hp
		self.damage = damage

	def attack(self, location):
		print(f'{self.name}유닛이 {location} 방향으로 적군을 {self.damage}만큼 공격합니다.')

	def damaged(self, damage):
		print(f'{self.name}유닛이 {damage}의 데미지를 입었습니다')
		self.hp -= damage
		print(f'{self.name}의 현재 체력은 {self.hp} 입니다')
		if self.hp <= 0:
			print(f'{self.name}은 파괴되었습니다')

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit('파이어뱃',50,16)
firebat1.attack('5시')
firebat1.damaged(25)
firebat1.damaged(25)