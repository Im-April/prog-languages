# 리스트[시작인덱스 : 끝인덱스]

items_db = [
    {'item_name':'Foo'},    # 인덱스 0
    {'item_name':'Bar'},    # 인덱스 1
    {'item_name':'Baz'},    # 인덱스 2
    {'item_name':'Roo'},    
    {'item_name':'Nar'},    
    {'item_name':'Zaz'},
    {'item_name':'Too'},    
    {'item_name':'Mar'},    
    {'item_name':'Aaz'},
    {'item_name':'Paz'}
]

# skip=0, limit=10인 경우:
# 인덱스 0부터 10 직전까지
print(items_db[0 : 0+10])
print()

# skip=1, limit=10인 경우:
# 인덱스 1부터 11 직전까지
print(items_db[1 : 1+10])
print()

# skip=2, limit=1인 경우
print(items_db[2 : 2+1])