customer = '난 직원이고 넌'

index = 5

while index >= 1:
    print(f'{customer} 고객님 :) 주문하신 아메리카노 나왔습니다. {index}번 남았습니다.')
    index -= 1
    if index == 0:
        print('커피는 폐기처리 되었습니다')

# customer = '꼴에 스벅 오신'
# while True:
#     print(f'{customer} 고객님 :) 주문하신 아메리카노 나왔습니다.') 무한루프

customer = '숨겨왔던 나의'
person = 'Unknown'

while person != customer:
    print(f'{customer} 고객님 :) 주문하신 아메리카노 나왔습니다. {index}번 남았습니다.')
    person = input('이름이 어떻게 되세요 ? ')