# 속성 추가하기

class Person :
    # __init__은 생성자 메서드로, 객체가 생성될 때 자동으로 호출
    def __init__(self, name, age) :
        self.name = name # 인스턴스 속성
        self.age = age

person1 = Person('홍길동',25)
person2 = Person('김철수',35)

print(person1.name)
print(person2.age)