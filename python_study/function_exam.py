def get_full_name(first_name: str, last_name: str): # 타입 힌트
    '''
    함수 실행 순서
    - first_name과 last_name를 받습니다.
    - title()로 각 첫 문자를 대문자로 변환시킵니다.
    - 두 단어를 중간에 공백을 두고 연결합니다.
    '''
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name('john','doe'))

def get_name_with_age(name: str, age: int) :
    name_with_age = name + " is this old : " + str(age)
    return name_with_age

print(get_name_with_age('maru', 2))