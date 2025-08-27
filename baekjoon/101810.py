n, m = map(int, input().split())

baskets = [0] * n

# M번 공 넣기 작업
for _ in range(m):
    i, j, k = map(int, input().split())
    
    for basket_num in range(i, j + 1):
        baskets[basket_num - 1] = k  # basket_num - 1로 인덱스 조정

# 결과 출력
print(*baskets)