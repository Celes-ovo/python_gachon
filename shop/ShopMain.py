# main

import ProductDAO as dao
from Product import *

print('### Mint auction v1.0 ###')

# 필요한 기능 1 : 우선 전체 상품들의 목록을 뱉어내야 함.

# python의 새로운 기능 1 : 이 변수는 이런 타입입니다 하고 지정해줄 수 있음
p : Product

for p in dao.getAll():
    print(f'[{p.id}]{p.name}\t{p.price}')


print('--------------------------')

# 기능 2 : 장바구니에 추가하는 기능을 만들어야 함.
import Cart as cart

sel = input('Type your code : ')
cart.add(sel)

print(f'{dao.get(sel)} has been added.')