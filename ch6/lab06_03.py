import random

count = 0
dice_1, dice_2, dice_3 = 0, 0, 0


while True:
    count += 1

    dice_1 = (random.randint(1, 6))
    dice_2 = (random.randint(1, 6))
    dice_3 = (random.randint(1, 6))

    if dice_1 == dice_2 and dice_2 ==  dice_3:
        break

    print("같은 숫자 %d가 나오기까지 총 %d번 던졌습니다."  % (dice_1, count))