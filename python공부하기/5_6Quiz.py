'''
당신은 Cocoa 서비스를 이용하는 택시 기사님 입니다.
50명의 숭객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

조건 1: 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다
조건 2: 당신은 소여 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[o] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[o] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2분
'''

from random import *

total_customer = 0

for customer in range(1,51):
    time_minute = random.randrange(5,51)

    if 5 <= time_minute <= 15:
        print(f"[⭕] {customer}번째 손님 (소요시간 : {time_minute}분) ")
        total_customer += 1
    else: # 매칭 실패한 경우
        print(f'[❌] {customer}번째 손님 (소요시간 : {time_minute}분)')


print(f"총 탑승 승객 : {total_customer} 분")