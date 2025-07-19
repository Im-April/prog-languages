class Unit:
	def __init__(self, name, hp, damage):  # 파이썬에서 클래스의 생성자 메서드. 인스턴스를 만들 때 자동으로 호출되며, 전달된 값의 개수와 순서가 일치해야 함.
		self.name = name
		self.hp = hp
		self.damage = damage
		print(f'{self.name} 유닛이 생성되었습니다.')
		print(f'체력 {self.hp}\t공격력 : {self.damage}')
		
# 클래스로부터 만들어지는 것을 '객체' 또는 '인스턴스'라고 한다.
marine1 = Unit('마린', 40, 5)
marine2 = Unit('마린', 45, 4)
tank = Unit('탱크', 150, 35)
