print('## Notepad v1.0 ##')

name = input('* Input your file name : ')
ext = input('Type your extension : ')

fname = name + ext

#print('Type your filename. (Exit : q)\n================================')

print('>>>')


with open(fname, 'w', encoding='utf-8') as fin:
    while(msg := input()) != '':

        if msg == 'q':
            break

        else:
            fin.write(msg+'\n')