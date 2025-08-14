# 계산 결과를 반환하는 함수
def add_numbers(a, b):
    result = a + b
    return result

# 함수의 결과를 변수에 저장
sum_result = add_numbers(10, 20)
print(f"10 + 20 = {sum_result}")

# 바로 사용도 가능
print(f"5 + 3 = {add_numbers(5, 3)}")

# 더 복잡한 계산 함수
def calculate_circle_area(radius):
    pi = 3.14159
    area = pi * radius * radius
    return area
print(f'반지름이 5인 원의 넓이 : {calculate_circle_area(5)}')

# 여러 값을 반환하는 함수