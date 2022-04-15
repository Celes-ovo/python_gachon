singer = {}

singer['이름'] = '노라조'
singer['구성원수'] = 9
singer['대표곡'] = '카레'


print(singer, '\n', '='*50)


for k in singer.keys():
    print(k, '==>', singer[k])