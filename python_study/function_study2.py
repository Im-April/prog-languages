# 매개변수가 있는 함수

def say_hello_to(name) :
    print(f'안녕하세요 {name}님!')

say_hello_to('마루')


# 여러 매개변수가 있는 함수
def instroduce_person(name, age, hobby) :
    print(f'이름 : {name}')
    print(f'나이 : {age}')
    print(f'취미 : {hobby}')

instroduce_person('마루',2,'산책')