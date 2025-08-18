N = int(input())
num = 1

for i in range(N) :
    print(' '*(N-num) + '*'*num)
    num+=1