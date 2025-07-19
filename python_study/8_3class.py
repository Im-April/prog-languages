class Unit:
	def __init__(self, name, hp, damage): 
		# 멤버변수 : 클래스 내에서 선언된 변수
		self.name = name
		self.hp = hp
		self.damage = damage
		print(f'{self.name} 유닛이 생성되었습니다.')
		print(f'체력 {self.hp}\t공격력 : {self.damage}')
		
# marine1 = Unit('마린', 40, 5)
# marine2 = Unit('마린', 45, 4)
# tank = Unit('탱크', 150, 35)

# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에서 보이지 않음)
wraith1 = Unit('레이스',80,5)
print(f'유닛이름 : {wraith1.name}, 공격력 : {wraith1.damage}')

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것
wraith2 = Unit('빼앗은 레이스',80,5)
wraith2.clocking = True # 추가로 외부에서 변수로 만들어 쓸 수 있음. 확장을 한 객체에 대해서만 적용

if wraith2.clocking == True:
	print(f'{wraith2.name}는 현재 클로킹 상태입니다.')