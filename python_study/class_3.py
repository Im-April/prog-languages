# 매서드 추가하기

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f'안녕하세요 저는 {self.name}이고 {self.age}살 입니다.'
    
    def have_birthday(self):
        self.age += 1
        print(f"{self.name}님이 생일을 맞아 {self.age}살이 되었습니다!")

person = Person("이영희", 28)
print(person.introduce()) 
person.have_birthday()     
