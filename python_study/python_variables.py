# 변수 선언과 할당

print('# 변수에 값 저장하기')
name = "김철수"      # 문자열
age = 25            # 정수
height = 175.5      # 실수
is_student = True   # 불린

print(name)
print(age)

pi = 3.141592
print(pi)
print(pi+2)
print(pi*2)
print(pi-2)
print(pi/2)

print('\n-----원의 둘레와 넓이 구하기-----')
pi = 3.14159265
r = 10

print(f'원주율 : {pi}')
print(f'반지름 : {r}')
print(f'원의 둘레 : {2*pi*r}')
print(f'원의 넓이 : {pi*r*r}')

print('\n# 변수 값 변경 하기')
score = 80
print(score)

score = 90
print(score)

score = score + 10
print(score)

print('\n# 올바른 변수명')
name = '김철수'
student_age = 20
lastName = '길동' # 카멜케이스
first_name = '홍' # 스네이크케이스 (파이썬 권장)
number1 = 100
_private = '숨김'

print('\n# 다중 할당')
print('-----한 줄로 여러 변수에 값 할당-----')
a,b,c = 1,2,3
print(a,b,c)

print('\n-----같은 값을 여러 변수에-----')
x = y = z = 0
print(x,y,z)

print('\n-----값 교환-----')
a,b = 10,20
a,b, = b,a # 값 교환
print(a,b)

print('\n# 변수 타입 확인')
name = "김철수"
age = 25
height = 175.5
is_adult = True

print(type(name))     # <class 'str'>
print(type(age))      # <class 'int'>
print(type(height))   # <class 'float'>
print(type(is_adult)) # <class 'bool'>

print('\n# 문자열 복합 연산자')
string_a = '안녕하세요'
print(string_a)
string_a += '!'
string_a += '!'
print(string_a)
string_a *= 2
print(string_a)

print('\n# 실용적인 변수 사용 예시')
print('-----1. 개인정보 관리-----')
student_name = '김영희'
korean_score = 85
english_score = 90
math_score = 78

# 총점과 평균 계산
total_score = korean_score + english_score + math_score
average_score = total_score / 3

print(f'학생 : {student_name}')
print(f'총점 : {total_score}\n평균 : {average_score}')

print('\n-----2. 쇼핑물 가격 계산-----')
product_name = "노트북"
original_price = 1500000
discount_rate = 0.15  # 15% 할인
tax_rate = 0.1        # 10% 세금

discount_amount = original_price * discount_rate
discounted_price = original_price - discount_amount
tax_amount = discounted_price * tax_rate
final_price = discounted_price + tax_amount 

print(f"상품: {product_name}")
print(f"할인 후 가격: {discounted_price}원")
print(f"최종 가격: {final_price}원")

print('\n-----3. 변수 재활용-----')
celsius = 25
fahrenheit = celsius * 9/5 + 32

print(f'섭씨 {celsius}도는 화씨 {fahrenheit}도 입니다.')

# 다른 온도로 변경
celsius = 0
fahrenheit = celsius * 9/5 + 32
print(f"섭씨 {celsius}도는 화씨 {fahrenheit}도입니다")