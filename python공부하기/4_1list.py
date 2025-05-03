# 지하철 칸별로 10명, 30명, 20명
subway = [10,30,20]
print(subway)

subway = ['김철수','이민수','최민지']
print(subway)

print(subway.index('이민수')) # 1 

# 다음 정류장에 이영희가 탐
subway.append('이영희') # 맨뒤에 나열된다
print(subway)

# 김철수와 이민수 사이에 김유진
subway.insert(1, '김유진')
print(subway)

# 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# 같은 이름의 사람 몇 명있는지 확인
subway.append('최민지')
print(subway)
print(subway.count('최민지'))

print('-'*50)

# 정렬 가능
num_list = [5,1,2,3,4]
#print(num_list.sort()) -> None이 반환
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

print('-'*50)

# 다양한 자료형과 함께 사용 가능
num_list2 = [5,1,2,3,4]
mix_list = ['마루',20,True]

num_list2.extend(mix_list)
print(num_list2)