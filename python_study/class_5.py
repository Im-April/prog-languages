class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount) :
        if amount > 0:
            self.balance += amount
            print(f"{amount}원이 입금되었습니다. 잔액: {self.balance}원")
        else:
            print("입금액은 0보다 커야 합니다.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}원이 입금되었습니다. 잔액: {self.balance}원")
        else :
            print("입금액은 0보다 커야 합니다.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액이 부족합니다.")
        elif amount > 0:
            self.balance -= amount
            print(f"{amount}원이 출금되었습니다. 잔액: {self.balance}원")
        else:
            print("출금액은 0보다 커야 합니다.")
    
    def get_balance(self):
        return f"{self.owner}님의 잔액: {self.balance}원"
    

account = BankAccount("홍길동", 10000)
print(account.get_balance())  # 홍길동님의 잔액: 10000원
account.deposit(5000)         # 5000원이 입금되었습니다. 잔액: 15000원
account.withdraw(3000)        # 3000원이 출금되었습니다. 잔액: 12000원