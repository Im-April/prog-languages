'''
if 조건식:
    실행할 코드

- 조건식이 True면 아래 코드 실행
- 조건식이 False면 실행 안 됨
- 들여쓰기 !!
'''

# Conditional Statements
if True:
    print('code1')
    print('code2')

print('code3')

age = 18

if age >= 18:
    print('성인 입니다.')
else:
    print('미성년자 입니다.')

score = 75

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('F')

num = 10

if num > 0:
    if num % 2 == 0:
        print('양수이면서 짝수입니다.')
    else:
        print('양수이면서 홀수입니다.')
else:
    print('0 또는 음수입니다.')

is_logged_in = True

if is_logged_in:
    print('로그인 성공')
else:
    print('로그인 실패')