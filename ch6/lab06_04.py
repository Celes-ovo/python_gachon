import random

user, com = 0, 0

for i in range(10):
    com = random.randint(1, 5)
    print(i, '번째')

    user =  int(input("숫자를 맞혀 보새요 : "))


    if user == com:
        print("정답입니다!")
        
        break


    else:
        print("오답입니다.")
        
        continue

print("Exit")