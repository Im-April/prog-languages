'''
타입으로서의 클래스
변수의 타입으로 클래스를 선언할 수도 있습니다.
'''

class Person :
    def __init__(self, name: str) :
        self.name = name

def get_person_name(one_person: Person) :
    return one_person.name

a = Person('김민수')
print(get_person_name(a))