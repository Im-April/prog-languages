A = int(input())  # 첫 번째 세 자리 수
B = int(input())  # 두 번째 세 자리 수

B_1 = B // 100
B_2 = (B % 100) // 10
B_3 = B % 10

print(B_3 * A)
print(B_2 * A)
print(B_1 * A)
print(A*B)
