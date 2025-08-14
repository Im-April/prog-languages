def calculate_age(birth_year, current_year=2025):
    '''
    출생연도로 나이 계산
    '''
    age = current_year - birth_year
    return age

# 성인인지 안닌지
def is_adult(birth_year) :
    age = calculate_age(birth_year)
    return age >= 20


print(f"1999년생의 나이: {calculate_age(1999)}살")
print(f"2010년생은 성인인가요? {is_adult(2010)}")