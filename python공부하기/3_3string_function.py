python = 'Python is Amazing'
print(python.lower())
print(python.upper())
print(python[0].isupper()) # True
print(len(python)) # 공백 포함
print(python.replace('Python','c'))

index = python.index('n')
#index = python.index('Java') -> 에러가 난다
print(index)

index = python.index('n', index+1) # 앞에서 찾은 위치 앞에서부터 n 찾기
print(index)

print(python.find('n'))
print(python.find('Java')) # -1을 반환


print(python.count('n')) # n이 몇번 나오는지