# 자료구조 변경
menu = {'커피','우유','주스'}
print(menu, type(menu)) # set

menu = list(menu)
print(type(menu)) # list

menu = tuple(menu)
print(type(menu)) # tuple

menu = set(menu)
print(type(menu))