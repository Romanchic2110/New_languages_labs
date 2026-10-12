class PasswordTooShortError(Exception):
    pass

class NotEnoughUppercaseError(Exception):
    pass

class NotEnoughLowercaseError(Exception):
    pass

class NotEnoughDigitsError(Exception):
    pass


def is_correct_password(password, /, *, length, upper, lower, numeric):
    if len(password) < length:
        raise PasswordTooShortError('Пароль короче допустимой длины')
    
    if sum(1 for i in password if i.isupper()) < upper:
        raise NotEnoughUppercaseError('Пароль содержит недостаточно заглавных букв')

    if sum(1 for c in password if c.islower()) < lower:
        raise NotEnoughLowercaseError('Пароль содержит недостаточно строчных букв')

    if sum(1 for c in password if c.isdigit()) < numeric:
        raise NotEnoughDigitsError('Пароль содержит недостаточно цифр')

    return True
