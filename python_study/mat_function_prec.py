# 두 수 입력받기
a, b = map(int, input('두 수를 입력하세요. : ').split())
print(a, b)

# 여러 수 입력받기
numbers = list(map(int, input('여러 수를 입력하세요. : ').split()))
print(numbers)

# 한 줄에 계산까지
print(sum(map(int, input('숫자를 입력하세요 : ').split())))