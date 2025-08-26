N = int(input())
list_A = list(map(int, input().split()))
v = int(input())

count = 0
for i in list_A:
    if i == v:
        count += 1

print(count)