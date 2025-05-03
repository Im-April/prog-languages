cabinet = {3:'마루',100:'똥마루'}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5]) -> 오류가 난다.
print(cabinet.get(5)) # None, 오류 안생김
print(cabinet.get(5, '사용 가능'))

print('-'*30)

print(3 in cabinet) # True
print(5 in cabinet) # False

print('-'*30)

cabinet = {'a-3':'마루','b-100':'콩이'}
print(cabinet['a-3'])
print(cabinet['b-100'])

# 새 손님
print(cabinet)
cabinet['a-3'] = '보리'
cabinet['c-20'] = '구름이'
print(cabinet)

print('-'*50)

# 간 손님
print(cabinet)
del cabinet['a-3']
print(cabinet)

print('-'*50)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 둘 다 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)
