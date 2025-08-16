H, M = map(int, input().split())

alarm = M - 45

if alarm < 0 :
    H -= 1
    if H < 0 :
        H = 23
    M = alarm + 60
    print(f'{H} {M}')
else :
    M = alarm
    print(f'{H} {M}')