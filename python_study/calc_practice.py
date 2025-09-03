print(10+5)
print(10-5)
print(10*5)
print(10/5)

print()

a=10
b=5
result = a+b
print(f'덧셈 : {a} + {b} = {result}')

result = a-b
print(f'뺄셈 : {a} - {b} = {result}')

result = a*b
print(f'곱셈 : {a} * {b} = {result}')

result = a/b
print(f'나눗셈 : {a} / {b} = {result}')

# 추가 연산자들 ...
a=10
b=3
result = a // b
print(f'정수 나눗셈 : {a} // {b} = {result}')

result = a % b
print(f'나머지연산 : {a} % {b} = {result}')

a=2
b=3
result = a ** b
print(f'거듭 제곱 : {a} ** {b} = {result}')

print()

# 예제 
# 간단한 계산기 만들기

num1 = float(input('첫 번째 숫자 입력 : '))
num2 = float(input('두 번째 숫자 입력 : '))

print(f'덧셈 : {num1} + {num2} = {num1 + num2}')
print(f'뺄셈 : {num1} - {num2} = {num1 - num2}')
print(f'덧셈 : {num1} * {num2} = {num1 * num2}')

if num2 != 0 :
    print(f'나눗셈 : {num1} / {num2} = {num1 / num2}')
else :
    print('0으로 나눌 수 없습니다.')


# 복합 계산 예제
x = 5
y = 3
z = 2

result = (x+y)*z**2 # 괄호와 연산 우선순위
print(f"(5 + 3) * 2^2 = {result}")  # 32

# 평균 계산
scores = [85, 92, 78, 96, 88]
average = sum(scores) / len(scores)
print(f"평균: {average}")  # 87.8