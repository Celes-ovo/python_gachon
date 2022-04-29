# 1
num1 = 100
num2 = 200

# 2
100 = num1 + num2
# >>> SyntaxError: cannot assign to literal

# 3
num1 + num2 = 100
# >>> SyntaxError: cannot assign to operator

# 4
3a = 10
# >>> SyntaxError: invalid syntax

# 5
num3 = 1000000000000000

# 6
if num1>num2:
result = num1 + num2

# 7
calc(10, 20)
# >>> NameError: name 'calc' is not defined

# 8
def calc(n1, n2):
    return n1+n2

# calc(10, 20)
# >>> 30


# 9
for i in (0, 5, 1):
    print(i, end='\t')
# >>>  0      5      1


# 10
while (num2 < num1):
    num2--
    print('**')
# >>> SyntaxError: invalid syntax


# 11
print('num1={num1}, num2={num2}')
# >>> f formatter

## 11-2
print(f'num1={num1}, num2={num2}')
# >>> num1=100, num2=200

# 12
num4 = 100, 200
print(num4)
# >>> (100, 200)

# 13
for i in [10, 5, 3]:
    print(i, end='\t')
# >>> 10    5   3


# 14
def printAll():
    pass
# 아무것도 없을 때
# >>> IndentationError: expected an indented block

# 적어도 pass 이상의 내용이 안에 필요


# 15
def varTest():
    global num1
    num1 = 500
    num5 = 200
print(num5)


# 16
list2 = [i for i in range(1, 10)]
print(list2)