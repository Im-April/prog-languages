# 숫자형 (Number)
# 정수 (int)

print('-----int-----\n')
print(type(222))
print()
age = 35
temperature = -10
print(f'age의 값 : {age}\nage의 자료형 : {type(age)}')
print(f'temperature의 값 : {temperature}\ntemperature의 자료형 : {type(temperature)}')
print('\n-----float-----\n')
# 실수 (float)
height = 175.5
pi = 3.14159
print(f'height의 값 : {height}\nheight의 자료형 : {type(height)}')
print(f'pi의 값 : {pi}\npi의 자료형 : {type(pi)}')

print('\n# 기본 산술 연산자')
print('-----사칙연산자-----\n')
print(f'5 + 7 = {5+7}')
print(f'5 - 7 = {5-7}')
print(f'5 * 7 = {5*7}')
print(f'5 / 7 = {5/7}')

a = 10
b = 3
print(a+b)

price = 1000
tax = 100
total = price + tax
print(total)

print(10-3)

balance = 50000
withdraw = 15000
remaining = balance - withdraw
print(remaining)

print(10*3)

width = 5
height = 7
area = width * height
print(area)

print(10/3) # 3.3333333333333335
print(9/3) # 3.0 (정수로 나누어떨어져도 실수)

total_score = 285
subjects = 3
averrage = total_score / subjects
print(averrage)

print('\n-----정수 나누기 연산자 (몫 나눗셈)-----')
print(f'3 // 2 = {3//2}')

print(10//3)
print(17//3)

total_items = 127
items_per_page = 10
total_pages = total_items // items_per_page + (1 if total_items % items_per_page else 0)
print(total_pages)

print('\n-----나머지 연산자-----')
print(10%5)
print(17%5)
print(f'5 % 2 = {5%2}')

number = 7
if number % 2 == 0 :
  print('짝수')
else : 
  print('홀수')

print('\n-----거듭 제곱-----')
print(2 ** 3)
print(5 ** 2)
print(9 ** 0.5)

radius = 5
area = 3.14 * (radius ** 2)

print('\n-----복합 대입 연산자-----')
score = 100

score += 10   # score = score + 10 → 110
score -= 5    # score = score - 5  → 105  
score *= 2    # score = score * 2  → 210
score /= 3    # score = score / 3  → 70.0
score //= 2   # score = score // 2 → 35.0
score %= 4    # score = score % 4  → 3.0
score **= 2   # score = score ** 2 → 9.0

print('\n-----연산자의 우선 순위-----')
print(f'2+2-2*2/2*2 = {2+2-2*2/2*2}')
print(f'2-2+2/2*2+2 = {2-2+2/2*2+2}')

print('\n# 활용 예시')
print('\n-----1. 할인 계산-----')
original_price = 50000
discount_rate = 0.2  # 20% 할인
discount_amount = original_price * discount_rate
finale_price = original_price - discount_amount
print(f'원가 : {original_price}원\n할인가 : {finale_price}원')

print('\n-----2. 할인 계산-----')
total_seconds = 3665
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"{hours}시간 {minutes}분 {seconds}초")

print('\n-----3. 복리 계산-----')
principal = 1000000  # 원금
rate = 0.05         # 5% 이자율
years = 3           # 3년
finale_amount = principal * (1 + rate) ** years
print(f'원금 : {principal}원\n최종금액 : {finale_amount}원')