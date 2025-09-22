# 불리언 (Boolean)
# 참(True)과 거짓(False) 두 가지 값만 가지는 데이터 타입.

is_raining = True
is_sunny = False

print(is_raining)
print(is_sunny)

a = 5
b = 3

print(a == b)   # False
print(a != b)   # True
print(a > b)    # True
print(a < b)    # False
print(a >= 5)   # True
print(b <= 3)   # True

# 불리언 연산
x = 10

print(x > 5 and x < 20)  # True (둘 다 만족)
print(x < 5 or x == 10)  # True (둘 중 하나 만족)
print(not (x == 10))     # False (반대)

# 불리언 활용
age = 18

if age >= 18:
    print('성인 입니다.')
else:
    print('미성년 입니다.')

is_logged_in = True

if is_logged_in:
    print('접속 성공 !')
else : 
    print('로그인이 필요합니다.')


a = 1
b = 1

print(a == b)
print(1 == 2)
print(1 > 2)
print(1 < 2)
print(True)
print(False)