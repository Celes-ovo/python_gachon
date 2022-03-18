total = 0


coffee_buy = input("커피의 구입 수 : ")
coffee_sell = input("커피의 판매 수 : ")

gimbap_buy = input("삼각김밥의 구입 수 : ")
gimbap_sell = input("삼각김밥의 판매 수 : ")

banana_milk_buy = input("바나나 우유의 구입 수 : ")
banana_milk_sell = input("바나나 우유의 판매 수 : ")

bentou_buy = input("도시락의 구입 수 : ")
bentou_sell = input("도시락의 판매 수 : ")

cola_buy = input("콜라의 구입 수 : ")
cola_sell = input("콜라의 판매 수 : ")

kkang_buy = input("새우깡의 구입 수 : ")
kkang_sell = input("새우깡의 판매 수 : ")


# ==================================

total -= int(coffee_buy) * 500
total -= int(gimbap_buy) * 900
total -= int(banana_milk_buy) * 800
total -= int(bentou_buy) * 3500
total -= int(cola_buy) * 700
total -= int(kkang_buy) * 1000

total += int(coffee_sell) * 1800
total += int(gimbap_sell) * 1400
total += int(banana_milk_sell) * 1800
total += int(bentou_sell) * 4000
total += int(cola_sell) * 1500
total += int(kkang_sell) * 2000

# ==================================


print("오늘의 총 매출액은 %d 원입니다." % total)