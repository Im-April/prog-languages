def deposit(balance, money): # 입금 함수수
    print(f'입금이 완료되었습니다. 잔액은 {balance+money}원 입니다.')
    return balance+money


deposit(0,50000)
print(deposit(0,50000))



def withdraw(balance, money): #출금
    if balance >= money:
        print(f'출금이 완료되었습니다. 잔액은 {balance-money}원 입니다.')
        return balance-money
    else:
        print(f'출금이 완료되지 않았습니다. 잔액은 {balance}원 입니다.')
        return balance
    
print(withdraw(100000,50000))


def withdraw_nigth(balance, money): # 저녁에 출금
    commission = 100 # 수수료
    return commission, balance - money - commission


print(withdraw_nigth(10000,5000))

