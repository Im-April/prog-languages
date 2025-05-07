# 메소드 오버라이딩 : 부모클래스에서 정의한 메소드 말고 자식클래스에서 정의한 메소드를 쓰고싶을 때
# 메소드를 새롭게 정의해서 사용할수있음

# 일반유닛 (부모클래스)
class Unit:
    def __init__(self, name, hp, speed): 
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print('지상 유닛 이동')
        print(f'{self.name} : {location} 방향으로 이동합니다. 속도 :  {self.speed} ')
        

# 공격유닛 (자식클래스)
class AttackUnit(Unit): 
    def __init__(self, name, hp, speed, damage): 
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f'{self.name} 유닛이 {location} 방향으로 적군을 {self.damage}만큼 공격합니다.')

    def damaged(self, damage):
        print(f'{self.name} 유닛이 {damage}의 데미지를 입었습니다')
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
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, speed=0, damage=damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):  # 들여쓰기 수정
        print('공중 유닛 이동')
        self.fly(self.name, location)


# 유닛 생성 및 테스트
vulture = AttackUnit('벌처', 80, 10, 20)
battlecruiser = FlyableAttackUnit('배틀크루저', 500, 25, 3)

vulture.move('11시')
battlecruiser.move('9시')