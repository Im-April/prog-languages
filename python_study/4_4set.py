'''
집합 (set)
중복 안됨
순서 없음
'''

my_set = {1,2,3,3,3}
print(my_set)

java = {'마루','콩이','보리'}
python = set(['마루','구름이'])


# 교집합 (java와 python을 모두 하는 사람)
print(java & python)
print(java.intersection(python))

# 합집합 (java를 할 수 있거나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합(java는 할 줄 알지만 python은 못하는 개발자)
print(java-python)
print(java.difference(python))

# python을 할 줄 아는 사람이 늘어남
python.add('똥마루')
print(python)

# java를 까먹음
java.remove('똥마루')
print(java)