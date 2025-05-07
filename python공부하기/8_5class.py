# 일반유닛
class Unit:
	def __init__(self, name, hp): 
		# 멤버변수 : 클래스 내에서 선언된 변수
		self.name = name
		self.hp = hp
		

# 공격유닛
class AttackUnit(Unit): # 상속
	def __init__(self, name, hp, damage): 
		Unit.__init__(self,name,hp)
		self.damage = damage

	def attack(self, location):
		print(f'{self.name}유닛이 {location} 방향으로 적군을 {self.damage}만큼 공격합니다.')

	def damaged(self, damage):
		print(f'{self.name}유닛이 {damage}의 데미지를 입었습니다')
		self.hp -= damage
		print(f'{self.name}의 현재 체력은 {self.hp} 입니다')
		if self.hp <= 0:
			print(f'{self.name}은 파괴되었습니다')

# 메딕 : 의무병, 공격력이 없음

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit('파이어뱃',50,16)
firebat1.attack('5시')
firebat1.damaged(25)
firebat1.damaged(25)