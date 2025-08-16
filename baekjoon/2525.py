now_H, now_M = map(int, input().split())
cook_time = int(input())

total_minutes = now_M + cook_time

now_H += total_minutes // 60
now_M = total_minutes % 60

if now_H > 23:
    now_H = now_H % 24

print(f'{now_H} {now_M}')

'''
total_minutes = 30 + 100 = 130분

130 ÷ 60 = 2 나머지 10
- 몫 2 → 2시간 추가 → 14 + 2 = 16시  
- 나머지 10 → 최종 분 = 10분

결과: 16시 10분
'''