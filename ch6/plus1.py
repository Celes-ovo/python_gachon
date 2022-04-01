_uname = 'Ryan'
_password = '1234'


uname = input('# Type your ID : ')
password = input('# Type your password : ')

if((uname == _uname) and (password == _password)):
    print('> Login succeded')

else:
    print('[!] Check your ID or password.')