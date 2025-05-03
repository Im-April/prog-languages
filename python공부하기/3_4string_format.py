print('a'+'b') # ab
print('a','b') # a b

# 방법1
print('나는 %d살이고 싶다' % 20) # d는 정수값
print('나는 %s을 좋아해요' % 'Python') # s는 문자열
print('Apple은 %c로 시작해요' % 'A') # c는 하나의 문자

print('나는 %s살이고 싶다' % 20) # 값 출력은 할 수 있음

print('-'*40)

print('나는 %s색과 %s색을 좋아해요' % ('파란', '분홍'))

print('-'*40)

# 방법 2
print('나는 {}살이고 싶어요'.format(20))
print('나는 {}색과 {}색을 좋아해요'.format('파란','분홍'))
print('나는 {1}색과 {0}색을 좋아해요'.format('파란','분홍'))

print('-'*40)

# 방법 3
print('나는 {age}살이며, {color}색을 좋아해요'.format(age=20, color='분홍'))
print('나는 {age}살이며, {color}색을 좋아해요'.format( color='분홍',age=20))

print('-'*50)

# 방법 4
age = 27
color = '빨간'
print(f'나는 {age}살이 아니며, {color}색을 좋아합니다다')