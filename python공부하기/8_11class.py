'''
주어진 코드를 활용하여 부동산 프로그램을 작성하시오

(출력 예제)
총 3대의 매물이 있습니다
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년
'''

class House:
    def __init__(self, location, house_type, deal_type, price, competion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.competion_year = competion_year

    def show_detail(self):
        print(f'{self.location} {self.house_type} {self.deal_type} {self.price} {self.competion_year}')

houses = []
house1 = House('강남','아파트','매매','10억','200년')
house2 = House('마포','오피스텔','전세','5억','2007년')
house3 = House('송파','빌라','월세','500/50','2000년')
houses.append(house1)
houses.append(house2)
houses.append(house3)

print(f'총 {len(houses)}대의 매물이 있습니다.')
for house in houses:
    house.show_detail()