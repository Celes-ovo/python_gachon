# binary 파일 처리

with open('.\\gachon.png', 'rb') as f:
    byte = f.read(1)

    # byte는 앞에 b가 붙음!
    while byte != b'':
        print(byte)
        byte = f.read(1)



# file copy
with open('.\\gachon.png','rb') as f, open('.\\c_gachon.png','wb') as t:
    byte = f.read(1)

    # byte는 앞에 b가 붙음!
    while byte != b'':
        print(byte)
        t.write(byte)
        byte = f.read(1)



# 코드 개선
with open('.\\gachon.png', 'rb') as f, open('.\\c2_gachon.png', 'wb') as t:
    while(byte := f.read(1)) != b'':
        print(byte)
        t.write(byte)

        ### +) t.write(str(byte))로 하면?