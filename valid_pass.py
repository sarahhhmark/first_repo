valid_password = False
while valid_password is False:
    password = input('Введите пароль: ')
    if len(password) >= 8:
        if password.upper() != password and password.lower() != password:
            print('Корректный пароль')
            valid_password = True
        else:
            print('Некорректный пароль')
    else:
        print('Некорректный пароль')