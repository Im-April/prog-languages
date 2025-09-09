# 문자열 (String)
print('\n-----str-----\n')
print(type('안녕하세요'))
print()

name = '홍길동'
message = '안녕하세요'
long_text = """여러 줄에 걸친
긴 문자열입니다."""

print(f'name의 값 : {name}\nname의 자료형 : {type(name)}')
print(f'message의 값 : {message}\nmessage의 자료형 : {type(message)}')
print(f'long_text의 값 : {long_text}\nlong_text의 자료형 : {type(long_text)}')

print('\n-----교재 예시-----\n')
print('# 하나만 입력합니다.')
print('Hello Python Programming...!')

print('\n# 여러 개 출력합니다.')
print(10,20,30,40)
print('안녕하세요','저는','홍길동','입니다 !')
print('\n# 큰/작은 따옴표로 문자열 만들기')
print('안녕하세요 작은 따옴표로 문자열 만들었습니다.')
print("안녕하세요 큰 따옴표로 문자열 만들었습니다.")

print('\n# 문자열 내부에 따옴표 넣기')
print('# 1. 다른 따옴표 사용하기')
print("제 이름은 '홍길동'입니다.")
print('\n# 2. 이스케이프 문자 사용하기')
print('제 이름은 \'홍길동\'입니다.')

print('\n# 이스케이프 문자 사용해보기')
print('\'안녕하세요\' 라고 말했습니다.')
print('\'줄바꿈\' : 첫 번째 줄\n두 번째 줄\n세 번째 줄')
print('\'탭 (들여쓰기) : \t들여쓰기\t!!')
print('\'백슬레시 출력\' : \\')
print('처리중...\r완료!') # 출력: 완료! (처리중... 위에 덮어씀)

print('\n 탭 사용해보기 !!')
print('이름\t나이\t지역')
print('윤인성\t12\t강서구')
print('윤아린\t21\t강서구')
print('구름\t3\t강서구')

print('\n-----문자열 연산자-----\n')
print('# 문자열 연산자 : +')
print('안녕'+'하세요')
first_name = '김'
last_name = '철수'
full_name = first_name + last_name
print(full_name)

print('\n# 문자열 연산자 : *')
print('안녕하세요'*3)
star = '*'
line = star * 10
print(line)
laught = '하'
big_laught = laught * 5
print(big_laught)

print('\n# 포함 연산자 : in')
text = '안녕하세요, 파이썬 공부중입니다.'
print('파이썬' in text) # True
print('자바' in text) # False

print('\n# 불포함 연산자 : not in')
forbidden_words = ["욕설", "비방", "광고"]
user_input = "안녕하세요 반갑습니다"

clean = True

for word in forbidden_words : 
  if word in user_input :
    clean = False
    break
print(clean)

print('\n-----문자 인덱싱-----\n')
print('# 교재 예시')
print('안녕하세요'[0])
print('안녕하세요'[1])
print('안녕하세요'[2])
print('안녕하세요'[3])
print('안녕하세요'[4])

print('\n# 양수 인덱스')
text = 'Python'
print(text[0])  # P
print(text[1])  # y  
print(text[2])  # t
print(text[5])  # n

print('\n# 음수 인덱스 : 뒤에서부터 -1부터 시작')
text = 'Python'
print(text[-1])  # n (마지막 문자)
print(text[-2])  # o (뒤에서 두 번째)
print(text[-6])  # P (첫 번째 문자)
print('안녕하세요'[-1])
print('안녕하세요'[-2])
print('안녕하세요'[-3])
print('안녕하세요'[-4])
print('안녕하세요'[-5])

print('\n# 문자열 범위 선택 : 슬라이싱')
print('안녕하세요'[1:4]) # 녕하세
print('안녕하세요'[:2]) # 안녕
print('안녕하세요'[2:]) # 세요

print('\n# 예시')
print('-----1. 이름에서 성과 이름 분리-----')
full_name = '김철수'
surname = full_name[0]
given_name = full_name[1:]
print(f'성 : {surname}\n이름 : {given_name}')

print('\n-----2. 파일 확장자 확인-----')
filename = "document.pdf"
extension = filename[-3:] # pdf
first_char = filename[0] # d
print(f'확장자 : {extension}')

print('\n-----3. 문자열 첫 글자와 마지막 글자-----')
word = '안녕하세요'
first_char = word[0]
last_char = word[-1]
print(f'첫 글자 : {first_char}\n마지막 글자 : {last_char}')

print('\n# ⚠️ 주의 사항')
print('-----1. 인덱스 범위 오류-----')
text = 'Hello'
# print(text[10])  # IndexError! 인덱스가 범위를 벗어남

# 안전한 방법
if len(text) > 10 :
  print(text[10])
else :
  print('범위를 벗어남')

print('\n-----2. 문자열은 변경 불가능-----')
text = "Hello"
# text[0] = "h"  # TypeError! 문자열은 직접 수정 불가

# 새로운 문자열 생성해야 함
new_text = 'h' + text[1:]
print(new_text)

print('\n# 연습 문제')
message = "안녕하세요파이썬"

print(f'첫 번째 문자 : {message[0]}')
print(f'마지막 문자 : {message[-1]}')
print(f'가운데 글자 : {message[len(message)//2]}')

print('\n# 문자열 길이 구하기')
print(len('안녕하세요'))

print('\n# 문자열 연산자의 우선순위')
print('안녕'+'하세요'*3)
print(('안녕'+'하세요')*3)
print('안녕'+('하세요'*3))

print('\n# 문자열의 format()함수')

name = '김철수'
age = 24

# {} 자리에 순서대로 값 들어감
message = '안녕하세요, {}님 나이는 {}살이군요.'.format(name, age)
print(message)

string_a = '{}'.format(10)
print(string_a)
print(type(string_a))

format_a = '{}만원'.format(5000)
format_b = '파이썬 열공하여 첫 연봉 {} 만 원 만들기'.format(5000)
format_c = '{} {} {}'.format(3000, 4000, 5000)
format_d = '{} {} {}'.format(1, '문자열', True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)

print('\n-----인덱스 지정-----')
text = "{0}님은 {1}살이고, {0}님의 취미는 독서입니다.".format("이영희", 30)
print(text)

print('\n-----키워드 사용-----')
info = '이름: {name}, 점수: {score}점'.format(name='김철수', score=80)
print(info)

# 정수
output_a = '{:d}'.format(52)

# 특정 칸에 출력하기
output_b = '{:5d}'.format(52) # 5칸
output_c = '{:10d}'.format(52) # 10칸

# 빈칸을 0으로 채우기
output_d = '{:05d}'.format(52)
output_e = '{:05d}'.format(-52)

print('# 기본')
print(output_a)
print('# 특정 칸에 출력하기')
print(output_b)
print(output_c)
print('# 빈칸을 0으로 채우기')
print(output_d)
print(output_e)

output_f = '{:+d}'.format(52) # 양수
output_g = '{:+d}'.format(-52) # 음수
output_h = '{: d}'.format(52) # 양수 : 기호 부분 공백
output_i = '{: d}'.format(-52) # 음수 : 기호 부분 공백

print('# 기호와 함께 출력하기')
print(output_f)
print(output_g)
print(output_h)
print(output_i)

print('\n# 조합하기')
a1 = '{:+5d}'.format(52)
a2 = '{:+5d}'.format(-52)
print(a1)
print(a2)

a3 = '{:=+5d}'.format(52)
a4 = '{:=+5d}'.format(-52)
print(a3)
print(a4)

a5 = '{:+05d}'.format(52)
a6 = '{:+05d}'.format(-52)
print(a5)
print(a6)

print('\n# 숫자 포맷팅')
print('----소수점 자리수-----')
pi = 3.141592653
print('원주율: {:.2f}'.format(pi))
print('원주율: {:.4f}'.format(pi))
print('{:15.3f}'.format(52.273))
print('{:15.2f}'.format(52.273))
print('{:15.1f}'.format(52.273))

print('----자릿수 맞추기-----')
number = 32
print('번호: {:03d}'.format(number)) # 3자리, 빈자리는 0으로
print('번호: {:5d}'.format(number)) # 5자리

exam = 52.273
print('{:f}'.format(exam))
print('{:15f}'.format(exam))
print('{:+15f}'.format(exam))
print('{:+015f}'.format(exam))

print('\n----의미 없는 소수점 제거하기-----')
a = 52.0
b = '{:g}'.format(a)
print(a)
print(b)

print('\n----천 단위 구분자-----')
big_num = 1234567
print('금액: {:,}원'.format(big_num))

print('\n----문자열 양 옆 공백 제거-----')
input_a = """
    안녕하세요
문자열 함수를 알아봅시다.
"""
print(input_a)
print(input_a.strip())

print('\n# 활용 예시')

print('\n----성적표 만들기-----')

name = "홍길동"
korean = 85
english = 92
math = 78
total = korean + english + math
average = total / 3

report = """
=== 성적표 ===
학생명: {name}
국어: {korean:3d}점
영어: {english:3d}점  
수학: {math:3d}점
-----------
총점: {total:3d}점
평균: {average:5.1f}점
""".format(name=name, korean=korean, english=english, 
           math=math, total=total, average=average)

print(report)

print('\n----상품 목록-----')
products = [
    ("사과", 2000, 10),
    ("바나나", 3000, 5), 
    ("오렌지", 2500, 8)
]

print("상품명    가격     수량")
print("-" * 20)
for name, price, quality in products:
  print('{:6s} {:,}원 {:2d}개'.format(name, price, quality))