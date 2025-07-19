# 일반유닛 (부모클래스)
class Unit:
    def __init__(self, name, hp, speed): 
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print('지상 유닛 이동')
        print(f'{self.name} : {location} 방향으로 이동합니다. 속도 :  {self.speed} ')

# 건물
class BuildingUnit(Unit):
	def __init__(self,name,hp,location):
		pass # 일단은 넘어가라


# 서플라이 디폿 : 건물 1개 건물 = 8 유닛.
supply_depot = BuildingUnit('서플라이 디폿',500,'7시')

def GameStart():
	print('[알림] 새로운 게임을 시작합니다.')

def GameOver():
	pass

GameStart()
GameOver()