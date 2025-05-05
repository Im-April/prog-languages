gun = 10 # 전역 변수

def checkpoint(soldiers) : 
	gun = 20 # 지역 변수
	gun = gun-soldiers
	print(f'[함수 내] 남은 총 : {gun}')

print(f'전체 총 : {gun}')
checkpoint(2)
print(f'남은 총 : {gun}')

print('-'*30)

def checkpoint1(soldiers) : 
	global gun # 전역 공간에 있는 gun 사용
	gun = gun-soldiers
	print(f'[함수 내] 남은 총 : {gun}')

print(f'전체 총 : {gun}')
checkpoint1(2)
print(f'남은 총 : {gun}')

print('-'*30)

def checkpoint2(gun,soldiers):
	gun = gun-soldiers
	print(f'[함수 내] 남은 총 : {gun}')
	return gun

gun = 10
print(f'전체 총 : {gun}')
gun = checkpoint2(gun,2)
print(f'남은 총 : {gun}')