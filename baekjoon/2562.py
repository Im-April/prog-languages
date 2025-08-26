try:
    list_a = []
    
    for i in range(9):  # 보통 백준에서 9개 입력받는 문제들이 있어요
        a = int(input())
        list_a.append(a)
    
    max_a = max(list_a)
    print(max_a)
    print(list_a.index(max_a) + 1)
    
except:
    pass