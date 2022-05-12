## 기본 파일 읽기

fin = open('./test.txt', 'r', encoding='utf-8')

while True:
    msg = fin.readline()
    
    if msg=='':
        break

    else:
        print(msg, end='')

fin.close()


## 새로운 문법

fin = open('./test.txt', 'r', encoding='utf-8')

while(msg := fin.readline()) != '':
    print(msg.strip())

fin.close()


## for문으로 file 내용을 읽어서 출력

fin = open('./test.txt', 'r', encoding='utf-8')

for msg in fin.readlines():
    print(msg.strip())

fin.close()




# ==================================================

## autoclose 사용하기 (★)

with open('test.txt', 'r', encoding='utf-8') as fin:
    for msg in fin.readlines():
        print(msg.strip())

# ===================================================



## 파일 전체를 하나의 문자열로

with open('./test.txt', 'r', encoding='utf-8') as fin:
    print(fin.read())

"""
다만 이 방법은

1. 한번에 불러오기 때문에 큰 파일을 불러올 경우 메모리 문제가 발생함
2. 불러온 전체 내용에 각 줄에 접근하려면 또다시 변수로 받는 등의 작업 필요

"""



# ===================================================
# ===================================================
# ===================================================


## 파일에 내용 추가 : append

with open('./test.txt', 'a', encoding='utf-8') as fin:
    fin.write('\nFlygon is the best')

with open('./test.txt', 'r', encoding='utf-8') as fin2:
    print(fin2.read())

"""
>>>
Hello!
This is for test.
Flygon is the best

"""


## write mode
with open('./test2.txt', 'w', encoding='utf-8') as fin:
    fin.write('Appending...')

with open('./test2.txt', 'r', encoding='utf-8') as fin2:
    print(fin2.read())

# append와 달리 write는 기존 내용을 모두 지우고 새 내용을 입력한다.