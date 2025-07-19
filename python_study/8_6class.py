# 다중 상속 : 부모가 2이상

# 일반유닛 (부모클래스)
class Unit:
	def __init__(self, name, hp): 
		# 멤버변수 : 클래스 내에서 선언된 변수
		self.name = name
		self.hp = hp
		

# 공격유닛 (자식클래스)
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

# 날 수 있는 기능
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f'{name} : {location} 방향으로 날아갑니다. 속도 : {self.flying_speed}')



# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
	def __init__(self,name,hp,damage,flying_speed):
		AttackUnit.__init__(self,name,hp,damage)
		Flyable.__init__(self,flying_speed)


# 발키리 : 공중공격유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit('발키리',200,6,5)
valkyrie.fly(valkyrie.name, "3시")