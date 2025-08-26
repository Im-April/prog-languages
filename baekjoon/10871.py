N, X = map(int,input().split())

A = list(map(int,input().split()))

list_a = []
for i in A :
    if i < X :
        list_a.append(i)

print(*list_a)