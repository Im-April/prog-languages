# 파이썬 내장함수들...

print('Hello') # 출력

# 입력
a = input('정수를 입력하세요 : ')
print(a)

# 길이
print(len([1,2,3]))

# 정수 변환
print("a의 타입 : ",type(a))
int_a = int(a)
print('int_a의 타입 :' ,type(int_a))

# 문자열 변환
str_a = str(int_a)
print('str_a의 타입 :' ,type(str_a))

# 맵 함수
# map(함수, 반복가능한객체)
c,d = map(int,['1','2'])
print(c,d)
print('c의 타입 :' ,type(c))
print('d의 타입 :' ,type(d))

# 합계
print(sum([1,2,3]))

# 최댓값
print(max([1,2,3]))

# 최솟값
print(min([1,2,3]))