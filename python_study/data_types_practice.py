# 단일 따옴표
text1 = 'Hello World'
print(text1)
print(type(text1))

# 이중 따옴표
text2 = "Hello World"
print(text2)
print(type(text2))

# 삼중 따옴표 (여러 줄)
text3 = """
이것은 여러 줄로
작성된 문자열입니다.
"""
print(text3)
print(type(text3))

# 빈 문자열
empty = ""
print(empty)
print(type(empty))

print('Hello')
print("Hello")
print('Hello "World"')
print("'Hello' World")

# 문자열 특성
text = "Python"
print(len(text))        # 6 (길이)
print(text[0])          # 'P' (첫 번째 문자)
print(text[-1])         # 'n' (마지막 문자)
print(text[1:4])        # 'yth' (슬라이싱)

print('Hello' + 'World')
print('Hello'*3)
print('Hello'[0])
print('Hello'[1])

print()
print('-----문자열 연산-----')

first = 'Hello'
second = 'World'

result = first + ' ' + second
print(result)

# 반복
repeat = 'Hi'*3
print(repeat)

# 멤버십 연산자
print("lo" in "Hello")  # True
print("Hi" in "Hello")  # False

print()
print('-----문자열 메소드-----')
text = "Hello World"

# 대소문자 변환
print(text.upper())
print(text.lower())
print(text.title()) # 각 단어의 첫 글자만 대문자, 나머지는 소문자로 변환
print(text.capitalize()) # 문자열의 첫 글자만 대문자, 나머지는 모두 소문자
print(text.swapcase()) # 대문자는 소문자로, 소문자는 대문자로

# 검색과 확인
text = "Python Programming"

# 검색
print(text.find("gram"))     # 10 (위치 반환, 없으면 -1)
print(text.index("gram"))    # 10 (위치 반환, 없으면 오류)
print(text.count("m"))       # 2 (개수)

# 시작/끝 확인
print(text.startswith('Py'))
print(text.endswith('ing'))

# 문자열 타입 확인
print('123'.isdigit()) # True, 문자열이 숫자(0~9)로만 구성
print("abc".isalpha()) # True, 문자열이 알파벳 문자로만 구성
print("abc123".isalnum()) # True, 문자열이 알파벳+숫자(문자와 숫자 혼합 가능) 로만 구성
print("   ".isspace()) # 공백 문자(space, tab, newline 등)만 있으면 True

# 문자열 분할과 결합
text = "apple,banana,orange"

# 분할
fruits = text.split(',')
print(fruits)

# 결합
joined = " | ".join(fruits)
print(joined)

# 줄 단위 분할
multiline = "첫째 줄\n둘째 줄\n셋째 줄"
lines = multiline.splitlines()
print(lines)

print()
print('-----공백 처리-----')

text = "  Hello World  "
print(text.strip()) # "Hello World" (양쪽 공백 제거)
print(text.lstrip()) # "Hello World  " (왼쪽 공백 제거)
print(text.rstrip()) # "  Hello World" (오른쪽 공백 제거)

# 특정 문자 제거
text2 = "***Hello***"
print(text2.strip("*"))     # "Hello"