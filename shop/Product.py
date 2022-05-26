# 상품 구조를 제공하는 class
# 상품의 코드, 제품의 정보, 가격에 대한 정보가 필요

class Product:

    def __init__(self, id, name, price):

        # self는 자동적으로 parameter가 전달됨.
        self.id = id
        self.name = name
        self.price = price




"""
class Product:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
"""