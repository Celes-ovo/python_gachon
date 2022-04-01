_uname = 'Ryan'
_password = '1234'

exit_num = 0

while True:
    uname = input('# Type your ID : ')
    password = input('# Type your password : ')

    if((uname == _uname) and (password == _password)):
        print('> Login succeded\n')
        exit()

    else:
        print('[!] Check your ID or password.\n')
        exit_num += 1

        if exit_num == 3:

            print('[Log]Shutdown\n')

            exit()