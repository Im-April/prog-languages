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