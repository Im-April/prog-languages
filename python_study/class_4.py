# 클래스와 속성과 인스턴스 속성

class Person:
    species = "호모 사피엔스"  # 클래스 속성 (모든 인스턴스가 공유)

    def __init__(self,name,age):
        self.name = name
        self.age = age

person1 = Person("홍길동", 25)
person2 = Person("김철수", 30)

print(person1.species)
print(person2.species)
print(person1.name)
print(person2.name)
