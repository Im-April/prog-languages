# 기본값이 있는 매개변수

# 기본값 설정
def greet_person(name, greeting='안녕하세요') :
    return f'{greeting}, {name}님!'

# 기본값 사용
print(greet_person('김민수'))

# 다른값 사용
print(greet_person('김민수','반가워요'))

# 세금 계산기
def calculate_price(price, tax_rate=0.1) :
    '''
    가격에 세금을 포함한 최종 가격을 계산
    '''
    total_price = price + (price * tax_rate)
    return total_price

print(f'1000원 상품 (기본 10% 세금) : {calculate_price(1000)}원')
print(f"1000원 상품 (5% 세금): {calculate_price(1000, 0.05)}원")