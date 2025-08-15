# 타입 매개변수를 활용한 Generic(제네릭) 타입

from typing import List

def process_items(items: List[str]) :
    for item in items :
        print(item)

fruits = ["사과", "바나나", "오렌지", "포도"]
process_items(fruits)

from typing import Tuple, Set

def process_items(items_t: Tuple[int, int, str], items_s: Set[bytes]):
    '''
    변수 items_t는, 차례대로 int, int, str인 tuple이다.
    변수 items_s는, 각 아이템이 bytes인 set이다.
    '''
    return items_t, items_s

my_t = (42, 100, 'hello')
my_s = {b"hello", b"world", b"python"}

result_tuple, result_set = process_items(my_t, my_s)
print(f"\n반환된 튜플: {result_tuple}")
print(f"반환된 셋: {result_set}")

from typing import Dict

def process_items(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

fruit_prices = {
    "사과": 1500.0,
    "바나나": 2000.0,
    "오렌지": 3000.0
}
process_items(fruit_prices)

from typing import Optional

def say_hi(name: Optional[str] = None) : # name은 문자열이거나 None일 수 있음
    if name is not None :
        print(f'Hye {name}')
    else :
        print('Hello world')

say_hi()
say_hi('maru')