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