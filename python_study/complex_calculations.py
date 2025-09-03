# 절댓값
print(abs(-5))
print(abs(3.14))

# 반올림
print(round(3.14159))
print(round(3.14159, 2))

# 최댓값, 최솟값
numbers = [1,2,3,4,5]
print(max(numbers))
print(min(numbers))

# 합계
print(sum(numbers))

# 거듭제곱
print(pow(2,3)) # 8 (2의 3제곱)
print(pow(2,3,5)) # 3 (2^3 % 5)

# 형변환
print(int(3.8))      # 3
print(float(5))      # 5.0
print(complex(3, 4)) # (3+4j)

print()

import math

# 올림
print(math.ceil(2.2)) # 3

# 내림
print(math.floor(2.2)) # 2

# 거듭제곱 
print(math.pow(2,10))

# 제곱근
print(math.sqrt(16)) 

# 원주율
print(math.pi)

# 자연로그의 밑 e
print(math.e)

# 삼각함수 
print(math.sin(math.pi/2))   # 1.0
print(math.cos(0))           # 1.0
print(math.tan(math.pi/4))   # 1.0

# 로그함수
print(math.log(10))          # 2.302585092994046 (자연로그)
print(math.log10(100))       # 2.0 (상용로그)
print(math.log(8, 2))        # 3.0 (밑이 2인 로그)

print()

# random 모듈
import random

# 기본 난수 생성
print(random.random())           # 0.0~1.0 사이 실수
print(random.randint(1, 10))     # 1~10 사이 정수
print(random.uniform(1.0, 10.0)) # 1.0~10.0 사이 실수

colors = ['red','blue','green','pink']
print(random.choice(colors)) # 랜덤선택
print(random.sample(colors,2)) # 2개 랜덤 선택 (중복 없음)

# 리스트 섞기
numbers = [1,2,3,4,5]
random.shuffle(numbers)
print(numbers)

print()
print('-'*40)

print('통계 계산 함수')
def  calculate_stats(numbers):
    n = len(numbers)
    total = sum(numbers)
    mean = total/n

    # 분산과 표준편차
    variance = sum((x-mean) ** 2 for x in numbers) / n
    std_dev = math.sqrt(variance)

    return {
        '개수': n,
        '합계': total,
        '평균': round(mean, 2),
        '최댓값': max(numbers),
        '최솟값': min(numbers),
        '분산': round(variance, 2),
        '표준편차': round(std_dev, 2)
    }

scores = [85, 92, 78, 96, 88, 75, 91]
stats = calculate_stats(scores)
for key, value in stats.items():
    print(f"{key}: {value}")


# 거리 계산 함수
def distance_2d(x1, y1, x2, y2):
    """2차원 평면에서 두 점 사이의 거리"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def distance_3d(p1, p2):
    """3차원 공간에서 두 점 사이의 거리"""
    return math.sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))

# 사용 예제
print(distance_2d(0, 0, 3, 4))  # 5.0
print(distance_3d((1, 2, 3), (4, 5, 6)))  # 5.196152422706632