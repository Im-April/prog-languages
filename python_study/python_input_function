print('# 기본 입력받기')
name = input()
print(name)

print('\n-----안내 메시지와 함께 입력받기-----')
name = input('이름을 입력하세요: ')
print(f'안녕하세요, {name}님')

say_hello = input('인사말을 입력하세요 : ')
print(say_hello)

print('-----input 함수 자료형-----')
age = input('나이를 입력하세요: ')
print(type(age))
print(age + '살')

height = float(input("키를 입력하세요(cm): "))
print(f"입력한 키: {height}cm")

number = input('숫자를 입력하세요 : ')
print(number)
print(type)

print('-----타입 변수-----')

# 숫자 입력받기
age_str = input('나이를 입력하세요 : ')
age = int(age_str)
print(f'10년 후 나이 : {age + 10}살')

# 한 줄로 작성
# age = int(input('나이를 입력하세요: '))

string_a = input("입력: ")
int_a = int(string_a)

string_b = input('입력: ')
int_b = int(string_b)

print(f'문자열 자료 : {string_a} {string_b}')
print(f'숫자 자료 : {int_a} {int_b}')

output_a = int('53')
output_b = float("5.5")

print(type(output_a), output_a)
print(type(output_b), output_b)

print('-----여러 값 한번에 입력-----')

numbers = input('숫자 3개를 공백으로 구분해서 입력하세요: ')
a,b,c = numbers.split() # 문자열로 분리
a,b,c = int(a), int(b), int(c) # 정수로 변환
print(f'합계 : {a+b+c}')

# 더 간단하게
a, b, c = map(int, input("숫자 3개 입력: ").split())
print(f"합계: {a + b + c}")

print('# 실용적인 예시들')
print('-----1. 간단한 계산기-----')

first_num = float(input('숫자를 입력하세요: '))
second_num = float(input('숫자를 입력하세요: '))
operator = input('연산자(+,-,*,/)')

if operator == '+':
  result = first_num + second_num
elif operator == '-':
  result = first_num - second_num
elif operator == '*':
  result = first_num * second_num
elif operator == '/':
  result = first_num / second_num
else:
  print('잘못된 연산자입니다.')

print(f'{first_num} {operator} {second_num} = {result}')

print('-----2. 개인정보 입력 프로그램-----')
name = input('이름을 입력하세요: ')
age = int(input('나이를 입력하세요: '))
email = input('이메일을 입력하세요: ')
phone = input('전화번호를 입력하세요: ')

print("\n=== 입력하신 정보 ===")
print(f"이름: {name}")
print(f"나이: {age}살")
print(f"이메일: {email}")
print(f"전화번호: {phone}")

print('-----3. 성적 계산기 프로그램-----')
student_name = input("학생 이름: ")
korean = int(input("국어 점수: "))
english = int(input("영어 점수: "))
math = int(input("수학 점수: "))

total = korean + english + math
average = total / 3

print(f'{student_name}학생의 성적')
print(f'총점 : {total}점')
print(f'평균 : {average}점')

if average >= 90 :
   grade = 'A'
elif average >= 80 :
   grade = 'B'
elif average >= 70 :
   grade = 'C'
elif average >= 60 :
   grade = 'D'
else :
   grade = 'F'

print(f'학점 : {grade}')

print('# 입력 오류 처리')
try:
  age = int(input('나이를 입력하세요: '))
  print(f'입력하신 나이 : {age}살')

except ValueError:
  print('숫자를 입력해주세요!')

print('-----반복해서 올바른 입력 받기-----')

while True:
  try:
    age = int(input('나이를 입력하세요: '))
    if age < 0 :
      print('양수를 입력하세요: ')
      continue
    break
  except ValueError:
    print('숫자를 입력해주세요!')

print(f'입력하신 나이 : {age}살')