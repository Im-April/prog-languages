print('# 리스트')
print('리스트 (List) - 순서가 있고 변경 가능')
fruits = ['사과','바나나','오렌지']
number = [1,2,3,4,5]
mixed = ['홍길동',25,True,3.14] # 다른 타입 섞어도 됨

print(fruits[0])    # 사과 (첫 번째)
print(fruits[-1])   # 오렌지 (마지막)
list_a = [[1,2,3],[4,5,6],[7,8,9]]
print(list_a)

print('\n-----리스트 조작-----')
fruits = ['사과','바나나']

fruits.append('오렌지')
fruits.insert(1,'포도')
print(fruits)

fruits.remove('포도') # 값으로 삭제
delected = fruits.pop() # 마지막 요소 삭제하고 반환
print(fruits)
print(delected)

fruits[0] = '청사과'
print(fruits)

print('리스트 요소 추가하기')
print('append, insert')
list_a =  [1,2,3]
print('리스트 뒤에 요소 추가하기')
list_a.append(4)
list_a.append(5)
print(list_a)
print()

print('리스트 중간에 요소 추가하기')
list_a.insert(0,0)
print(list_a)
print()

print('리스트 뒤에 여러 요소 추가하기')
list_a.extend([6,7,8])
print(list_a)
print()

print('리스트 요소 삭제하기: del, pop')
list_a = [0,1,2,3,4,5]
print(list_a)
print('리스트의 요소 하나 제거하기')
# 제거방법1. del
del list_a[1]
print(f'del list_a[1]: {list_a}')

# 제거방법2. pop
list_a.pop(2)
print(f'list_a.pop(2): {list_a}')
print()


print('\n-----리스트 인덱스-----')
list_a = [273, 32, 103, '문자열', True, False]
print(list_a[0])
print(list_a[1])
print(list_a[1:3]) # 32,103
list_a[0] = '변경'
print(list_a)
print(list_a[-1])
print(list_a[-2])
print('-----접근 연산자 이중으로 사용하기-----')
list_a = [273, 32, 103, '문자열', True, False]
print(list_a[3])
print(list_a[3][0]) # '문'
print(list_a) 
list_a = [[1,2,3],[4,5,6],[7,8,9]]
print(list_a)
print(list_a[1])
print(list_a[1][1]) # 5

print('\n-----리스트 연산자-----')
print('반복(*), 연결(+)')
list_a = [1,2,3]
list_b = [4,5,6]

print('리스트 출력')
print(f'list_a =  {list_a}')
print(f'list_b =  {list_b}')
print()

# 기본 연산자
print('리스트 기본 연산자')
print(f'list_a + list_b = {list_a + list_b}')
print(f'list_a * 3 = {list_a * 3}')
print()

# 함수
print('길이 구하기')
print(f'len(list_a) = {len(list_a)}')

print('\n# 연결 연산자와 요소 추가의 차이')
print('-----1. 리스트 연산자 사용하기-----')
list_a = [1,2,3]
list_b = [4,5,6]
list_plus = list_a + list_b
print(f'list_a: {list_a}\nlist_b: {list_b}\nlist_plus: {list_plus}')
print('리스트의 연산자는 원래 리스트에 변화를 가져오지 않는다.(비파괴적)')

print('\n-----2. 리스트 요소 추가 사용하기-----')
list_a = [1,2,3]
list_b = [4,5,6]
print(f'list_a: {list_a}\nlist_b: {list_b}')
list_a.extend(list_b)
print(f'list_a: {list_a}\nlist_b: {list_b}')
print('리스트의 요소 추가는 원래 리스트에 변화를 가져온다. (파괴적)')
