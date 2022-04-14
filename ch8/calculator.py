# 인자 : num1, num2, 사용할 operator

def calculator():
    num1 = int(input('1번째 숫자 : '))
    num2 = int(input('2번째 숫자 : '))

    operator = input('연산자(+, -, *, /) : ')

    if operator == '+':
        print('%d %s %d = %d' %(num1, operator, num2, num1+num2))
        
    elif operator == '-':
        print('%d %s %d = %d' %(num1, operator, num2, num1-num2))
        
    elif operator == '*':
        print('%d %s %d = %d' %(num1, operator, num2, num1*num2))
        
    elif operator == '/':
        print('%d %s %d = %f' %(num1, operator, num2, num1/num2))

# ====================================================================

calculator()