# Python의 타입 힌트를 사용해서 데이터 검증과 파싱을 해주는 강력한 라이브러리
# 일반 클래스: 데이터만 저장
# Pydantic 모델: 데이터를 저장 + 자동으로 검증 + 변환

from pydantic import BaseModel

class Person(BaseModel):  # BaseModel을 상속
    name: str
    age: int
    email: str

# 사용법
person = Person(name="김철수", age=25, email="kim@example.com")
print(person.name)