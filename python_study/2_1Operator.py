print(1+1)
print(4-2)
print(5*2)
print(6/3)
print('-'*20)

print(2**3) # 2의 3제곱
print(5%3) # 나머지 연산
print(10%3) #1
print(10//3) # 몫의 연산자
print('-'*20)

print(10>3)
print(4>=7)
print(10<3)
print(5<=5) # True
print('-'*20)

print(3 == 3) # 3은 3과 같다 -> True
print(4 == 2) #False
print( 1 != 3) # True
print(not (1 != 3)) # False
print('-'*20)

# and
print((3>0) and (3<5)) # 둘 다 참일 때 True
print((3>0) & (3<5))

#or
print((3>0) or (3>5)) # 둘 중에 하나라도 참이면 참
print((3>0) | (3>5))
print('-'*20)

print(5>4>3) # (5 > 4) and (4 > 3) -> True
print(5>4>7) # (5 > 4) and (4 > 7) -> False
