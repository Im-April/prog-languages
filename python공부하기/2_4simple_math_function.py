# 랜덤함수
from random import *

# print(random()) # 0.0 ~ 1.0 미만의 임의의 값을 생성
# print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값
# print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값
# print(int(random() * 10)+1) # 1 ~ 10 이하의 임의의 값

# 로또
print(int(random() * 45)+1) # 1 ~ 45 이하의 임의의 값

print(randrange(1,46)) # 1 ~ 45 이하의 임의의 값

print(randint(1,45) ) # 양 끝을 포함해서 임의의 값 생성