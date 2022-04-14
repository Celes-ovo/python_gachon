# camel case, snake case

from tkinter import N


def printAll():
    pass
# pass : 일단 내용은 나중에 쓰고 싶을 때...


# 인자가 하나인 함수를 만들 때
def printName(name):
    prtMsg = name + ' 님 안녕하세요!'

    print(prtMsg)


printName('최서아')


# 인자 하나와 return 함수
def printName2(name):
    prtMsg = name + ' 님 안녕하세요!'

    return prtMsg

a = printName2('김경윤')
print(a)


# 인자 2개
def calc(num1, num2):
    return (num1+num2)


# 인자는 3개이나, 마지막 3번째 인자의 값 지정
def calc2(num1, num2, num3=0):
    return num1+num2+num3


# ===================================================

# 가변 인자
def total(*num):
    tot = 0

    for n in num:
        tot += n

    return tot

print(total(1, 2, 3, 4, 5, 6, 7))


# ===================================================

# return이 여러 개인 경우
def addnum(*nums):
    tot = 0
    cnt = 0

    for i in nums:
        tot += i
        cnt += 1

    return cnt, tot


cnt, tot = addnum(10, 20, 30)
print(cnt, tot)



# 매개 변수 유형에 따른 값의 변화
num3 = 10
m = [1, 2, 3]

def varchange(num3, m):
    num3 += 1
    print('value of number : ', num3)

    m.append(num3)
    print(m)

varchange(num3, m)
print(num3)
print(m)


# 전역변수, 지역변수 : global keyword
num4 = 10

def var_test():
    global num4
    #num4=100

    print(num4)

var_test()