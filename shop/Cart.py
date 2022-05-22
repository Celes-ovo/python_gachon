# 장비구니

# class일 필요는 없음. 상품을 담아놓는 역할만 구현하면 됨.
list = []

def add(product):
    list.append(product)
    print(f'{product.name} 상품이 추가되었습니다.')

def getList():
    return list