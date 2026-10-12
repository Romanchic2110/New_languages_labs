class PasswordTooShortError(Exception):
    pass

class NoDigitsError(Exception):
    pass

class NoLowerCaseError(Exception):
    pass

class NoUpperCaseError(Exception):
    pass


def validate_passwords(passwords):
    exc_list = []
    
    for i, password in enumerate(passwords):
        if not isinstance(password, str):
            err = TypeError('Пароль не является строкой')
            err.add_note(f'Ошибка в пароле с индексом {i}')
            exc_list.append(err)
            continue
        
        password_errors = []
        
        if len(password) < 8:
            password_errors.append(PasswordTooShortError('Пароль слишком короткий'))
        
        if not any(c.isdigit() for c in password):
            password_errors.append(NoDigitsError('В пароле нет цифр'))
        
        if not any(c.islower() for c in password):
            password_errors.append(NoLowerCaseError('В пароле нет строчных букв'))
        
        if not any(c.isupper() for c in password):
            password_errors.append(NoUpperCaseError('В пароле нет заглавных букв'))
        
        for err in password_errors:
            err.add_note(f'Ошибка в пароле с индексом {i}')
        
        exc_list.extend(password_errors)
    
    if exc_list:
        raise ExceptionGroup('Некоторые пароли являются некорректными', exc_list)
    
    return True

