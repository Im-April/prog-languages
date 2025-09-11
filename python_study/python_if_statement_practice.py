print('# Boolean')
print(True)
print(False)
print(type(True))
print(type(False))

print('-----비교 연산자-----')
print(10 == 10)
print(10 != 100)
print(10 < 100)
print(10 > 100)
print(10 <= 100)
print(10 >= 100)

a = 10
b = 5

print(a > b)   # True (크다)
print(a < b)   # False (작다)
print(a >= b)  # True (크거나 같다)
print(a <= b)  # False (작거나 같다)
print(a == b)  # False (같다)
print(a != b)  # True (같지 않다)

print('가방' == '가방')
print('가방' != '하마')
print('가방' <= '하마') # 가나다순으로 앞에 있는 것이 작은 값
print('가방' >= '하마')

print('\n-----논리 연산자-----')
print(not True)
print(not False)

x = 10
under_20 = x < 20
print(f'under_20: {under_20}')
print(f'not under_20: {not under_20}')
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

age = 25
has_liecense = True

if age >= 18 and has_liecense:
  print('운전할 수 있습니다.')
else :
  print('운전할 수 없습니다.')

weather = '비'
if weather =='비' or weather == '눈':
  print('우산을 챙기세요')
else :
  print('좋은 날씨네요')

is_weekend = False

if not is_weekend:
  print('평일입니다. 일하러 가야죠!')
else:
  print('주말입니다. 쉬세요!')

print('\n# if 조건문')
print('-----기본 if문-----')
age = 20

if age >= 18:
  print('성인 입니다.')
  print('투표할 수 있어요')

number = 20

if number > 0:
  print('양수입니다.')
if number < 0:
  print('음수입니다.')
if number == 0:
  print('0입니다.')

print('날짜/시간과 관련된 기능')
import datetime

now = datetime.datetime.now()

print(f'{now.year} 년')
print(f'{now.month} 월')
print(f'{now.day} 일')
print(f'{now.hour} 시')
print(f'{now.minute} 분')
print(f'{now.second} 초')

print('{}년 {}월 {}일 {}시 {}분 {}초'.format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second))

if now.hour < 12 :
  print('현재 시각은 {}시로 오전입니다!'.format(now.hour))

if now.hour >= 12:
  print('현재 시각은 {}시로 오후입니다!'.format(now.hour))

if 3 <= now.month <= 5:
  print('이번 달은 {}월로 봄입니다'.format(now.day))
if 6 <= now.month <= 8:
  print('이번 달은 {}월로 여름입니다'.format(now.month))
if 9 <= now.month <= 11:
  print('이번 달은 {}월로 가을입니다'.format(now.month))
if now.month == 12 or 1 <= now.month <= 2:
  print('이번 달은 {}월로 가을입니다'.format(now.month))  
number = '12'
last_character = number[-1]
last_number = int(last_character)

if last_number == 0 or last_number == 2 or last_number == 4 or last_number == 6 or last_number == 8:
  print('짝수입니다.')

if last_number == 1 or last_number == 3 or last_number == 5 or last_number == 7 or last_number == 9:
  print('홀수입니다.')

number = '52'
last_character = number[-1]

if last_character in '02468':
  print('짝수입니다.')
if last_character in '13579':
  print('홀수입니다.')

number = '52'
number_int = int(number)

if number_int % 2 == 0:
  print('짝수입니다')
if number_int % 2 != 0:
  print('홀수입니다.')

print('\n-----if else문-----')
score = 85

if score >= 60:
  print('합격입니다.')
else :
  print('불합격입니다.')

number = '52'
number_int = int(number)

if number_int % 2 == 0:
  # 조건이 참일 때, 즉 짝수 조건
  print('짝수입니다')
else :
  # 조건이 거짓일 때, 즉 홀수 조건
  print('홀수입니다.')

print('\n-----if-elif-else (여러 조건)-----')
score = 85

if score >= 90:
  grade = 'A'
elif score >= 80:
  grade = 'B'
elif score >= 70:
  grade = 'C'
elif score >= 60:
  grade = 'D'
else :
  grade = 'F'

print(f'학점: {grade}')

print('\n#실용적인 예시들')
print('-----1. 로그인 시스템-----')
correct_id = 'admin'
correct_password = '1234'

user_id = 'admin'
user_password = '1234'

if user_id == correct_id and user_password == correct_password:
  print('로그인 성공')
  print('환영합니다')
elif user_id == correct_id:
  print('비밀번호가 틀렸습니다.')
else :
  print('존재하지 않는 아이디입니다.')

print('-----2. BMI 계산기-----')
height = float(input("키(cm): ")) / 100  # m로 변환
weight = float(input("체중(kg): "))

bmi = weight / (height ** 2)

print(f'BMI: {bmi:.1f}')

if bmi < 18.5:
  print('저체중 입니다')
elif bmi < 23:
  print('정상체중 입니다.')
elif bmi < 25:
  print('과체중 입니다.')
else:
  print('비만입니다.')

print('-----3. 계산기-----')
num1 = float(input("첫 번째 숫자: "))
operator = input("연산자(+, -, *, /): ")
num2 = float(input("두 번째 숫자: "))

if operator == '+':
  result = num1 + num2
elif operator == '-':
  result = num1 - num2
elif operator == '*':
  result  = num1 * num2
elif operator == '/':
  if num2 != 0:
    result = num1 / num2
  else:
    print('0으로 나눌 수 없습니다')
    result = None
else :
  print('잘못된 연산자 입니다.')
  result = None

if result is not None:
 print(f"결과: {num1} {operator} {num2} = {result}")

 print('-----4. 나이별 영화 관람 등급-----')
 age = int(input("나이를 입력하세요: "))
movie_rating = input("영화 등급(전체, 12, 15, 청불): ")

if movie_rating == "전체":
    print("관람 가능합니다.")
elif movie_rating == "12":
    if age >= 12:
        print("관람 가능합니다.")
    else:
        print("12세 이상만 관람 가능합니다.")
elif movie_rating == "15":
    if age >= 15:
        print("관람 가능합니다.")
    else:
        print("15세 이상만 관람 가능합니다.")
elif movie_rating == "청불":
    if age >= 18:
        print("관람 가능합니다.")
    else:
        print("18세 이상만 관람 가능합니다.")
else:
    print("잘못된 등급입니다.")

print('-----5. 중첩 조건문-----')
weather = input("날씨는? (맑음/비/눈): ")
temperature = int(input("온도는? "))

if weather == '맑음':
  if temperature >= 25:
    print('반팔을 입으세요')
  elif temperature >= 15:
    print('길팔을 입으세요')
  else:
    print('자켓을 입으세요')
elif weather == '비':
  print('우산을 가져가세요')
  if temperature <= 10:
    print('따듯하게 입으세요')
else :
  print('따듯하게 입고 조심히 다니세요')