print('# 변수 기본 문법')

x = 10
y = 5
print(x+y)

title = 'python'
print(f'Title is {title}')

# 선언과 할당
x = 10       # 정수형 변수
name = "Tom" # 문자열 변수
pi = 3.14    # 실수형 변수

'''변수 이름 규칙
- 문자, 숫자, 밑줄 사용 가능
- 숫자로 시작 못함
- 대소문자 구분
- 예약어는 변수 이름으로 사용 못함
'''

age = 25
user_name = "Alice"
pi_value = 3.14159

# 여러 변수 한번에 할당
a,b,c = 1,2,3
print(f'a = {a}, b = {b}, c = {c}')

# 같은 값 여러 변수에 할당
x = z = y = 0
print(f'x = {x}\ny = {y}\nz = {z}')

# 변수 타입 확인
x = 10
print(type(x))
print(x)

# 변수 값 교환
a, b = 5, 10
print(f'a = {a}\nb = {b}')

a, b = b, a
print(f'a = {a}\nb = {b}')

print()
print('# 변수를 사용하는 이유')

'''
1. 값을 재사용하기 위해
2. 코드를 이해하기 쉽게 만들기 위해
3. 값을 쉽게 변경하기 위해
4. 복잡한 데이터를 관리하기 위해
'''
name = '회원'
print(f'안녕하세요 {name}님')
print(f'{name}님을 위한 강의가 준비되었습니다.')
print(f'{name}님 꼭 참석 부탁드립니다.')

# 변수는 코드의 재사용성, 가독성, 유지보수성을 높이는 도구

pi = 3.14159
radius = 10

area = pi * radius * radius   # 원의 넓이
circumference = 2 * pi * radius   # 원의 둘레

print(f'원의 넓이 : {area}')
print(f'원의 둘레 : {circumference}')

# 값의 변경이 필요한 경우
score = 45
print(f'현재의 점수 : {score}')

score = score + 10
print(f'보너스 후 점수 : {score}')

print()
print('# 수 계산에서 변수의 사용')

donation = 200
student = 10
sponsor = 100

print((donation*student)/sponsor)

# 사칙연산
a = 15
b = 4

print(f'덧셈 : a + b = {a+b}')
print(f'뺄셈 : a - b = {a-b}')
print(f'곱셈 : a * b = {a*b}')
print(f'나눗셈 : a / b = {a/b}')
print(f'몫 : a // b = {a//b}')
print(f'나머지 : a % b = {a%b}')

# 평균 구하기
score1 = 80
score2 = 90
score3 = 100

average = (score1 + score2 + score3) / 3
print(f'평균 점수 : {average}')

# 단위 변환
cm = 187
meter = cm/100
print("키(미터):", meter)  # 1.87

# 이자 계산
principal = 100000  # 원금
rate = 0.05         # 이자율 5%
years = 3

interest = principal * rate * years
print(f'3년 뒤 이자 : {interest}')

# 물리 계산
distance = 150  # km
time = 3        # 시간

speed = distance / time
print(f'평균 속도 : {speed} km/h')

# 게임 점수 계산
base_score = 100
bonus = 50
combo = 3

total_score = (base_score + bonus) * combo
print(f'총 점수 : {total_score}')