# 데이터 처리를 담당
"""
초기 데이터가 있어야 하고, 상품들의 정보에 액세스 가능해야 함.

1. 상품 데이터를 등록하는 것.
2. 전체 상품의 데이터를 가져오는 것.
3. 특정 상품 하나의 데이터를 가져오는 것.

"""

products = {}

import Product
# from Product import *

products['101'] = Product('101', 'Galaxy', '1,000,000')
products['102'] = Product('102', 'Iphone 12', '1,250,000')
products['103'] = Product('103', 'LG V50', '750,000')


def getAll():
    return products.values()

# id 값을 받아서 해당 id에 해당하는 객체를 찾아 return해 주는 기능을 만들어야 함.
def get(id):
    return products[id]