chicken = 10
waiting = 1

class SoldOuitError(Exception):
    pass


while(True) :
    try:
        print(f'남은치킨 : {chicken}')
        order = int(input('치킨 몇 마리 주문하시겠습니까 ?'))
        if order > order:
            print('재료가 부족합니다.')
        elif order <= 0:
            raise ValueError
        else:
            print(f'[대기번호 {waiting}] {4}마리 주문이 완료되었습니다.')
            waiting += 1
            chicken -= order
        
        if chicken == 0:
            raise SoldOuitError
        
    except ValueError:
        print('잘못된 값을 입력하였습니다.')

    except SoldOuitError:
        print('제고가 소진되어 더 이상 주문을 받지 못합니다.')
        break