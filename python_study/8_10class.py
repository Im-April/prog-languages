from random import *

# 일반 유닛 
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f'{self.name} 유닛이 생성되었습니다.')

    def move(self, location):
        print('지상 유닛 이동 !')
        print(f'{self.name} : {location} 방향으로 이동합니다 속도 : {self.speed}')

    def damaged(self, damage):
        print(f'{self.name} : {damage} 데미지를 입었습니다')
        self.hp -= damage
        print(f'{self.name}  : 현재 체력은 {self.hp} 입니다.')
        if self.hp <= 0:
            print(f'{self.name} : 파괴되었습니다')


# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f'{self.name}이 {location} 방향으로 적군을 공격합니다. [공격력 : {self.damage}]')


# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, '마린', 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f'{self.name}이(가) 스팀팩을 사용합니다 (HP 10 감소)')
        else:
            print(f'{self.name} : 체력이 부족하여 스팀팩을 사용하지 않습니다')


# 탱크
class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, '탱크', 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if not Tank.seize_developed:
            return

        if not self.seize_mode:
            print(f'{self.name} : 시즈모드로 전환')
            self.damage *= 2
            self.seize_mode = True
        else:
            print(f'{self.name} : 시즈모드 해제')
            self.damage //= 2
            self.seize_mode = False


# 날 수 있는 기능 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f'{name}이 {location} 방향으로 날아갑니다 속도 : {self.flying_speed}')


# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 속도 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("공중 유닛 이동!")
        self.fly(self.name, location)


# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, '레이스', 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked:
            print(f'{self.name} : 클로킹 모드 해제합니다')
            self.clocked = False
        else:
            print(f'{self.name} : 클로킹 모드 설정합니다')
            self.clocked = True


# 게임 실행 함수
def game_start():
    print('[알림] 새로운 게임을 시작합니다.')


def game_over():
    print('Player : GG')
    print('[Player] 님이 게임에서 퇴장하셨습니다.')


# 게임 실행
game_start()

# 유닛 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()
t1 = Tank()
t2 = Tank()
w1 = Wraith()

# 유닛 일괄 관리
attack_units = [m1, m2, m3, t1, t2, w1]

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 시즈모드 개발
Tank.seize_developed = True
print('[알림] 탱크 시즈모드 개발이 완료되었습니다.')

# 공격 모드 준비
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21))

# 게임 종료
game_over()

