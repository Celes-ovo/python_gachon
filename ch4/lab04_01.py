twice = "트와이스"

for i in range(len(twice)):
    
    a = -(i+1)

    # end = '' : 다음 행으로 print 문자열이 자동으로 넘어가는 것을 방지해 줌.
    print(twice[a], end = '')

    if a < -4:
        break