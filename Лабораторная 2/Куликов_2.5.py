class AlreadyLoggedInError(Exception):
    pass

class IncorrectPasswordError(Exception):
    pass

class NotLoggedInError(Exception):
    pass


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self._logged_in = False
    
    def login(self, password):
        if self._logged_in:
            raise AlreadyLoggedInError(f"Пользователь '{self.username}' уже авторизован")
        
        if password != self.password:
            raise IncorrectPasswordError('Неверный пароль')
        
        self._logged_in = True
        print(f"Пользователь '{self.username}' успешно авторизован")
    
    def logout(self):
        if not self._logged_in:
            raise NotLoggedInError(f"Пользователь '{self.username}' не авторизован")
        
        self._logged_in = False
        print(f"Пользователь '{self.username}' вышел из системы")


user = User('secure', 'secure123')
user.login('secure123')

try:
    user.login('secure123')
except AlreadyLoggedInError as e:
    print(e)
    print(type(e))