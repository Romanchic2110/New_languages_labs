class BookAlreadyExistsError(Exception):
    pass

class BookNotFoundError(Exception):
    pass

class BookNotAvailableError(Exception):
    pass

class BookNotBorrowedError(Exception):
    pass


class Library:
    def __init__(self):
        self._books = {}
    
    def add_book(self, title):
        if title in self._books:
            raise BookAlreadyExistsError(f"Книга '{title}' уже есть в библиотеке")
        self._books[title] = False

    def borrow_book(self, title):
        if title not in self._books:
            raise BookNotFoundError(f"Книга '{title}' отсутствует в библиотеке")
        if self._books[title]:
            raise BookNotAvailableError(f"Книга '{title}' уже выдана")
        self._books[title] = True
    
    def return_book(self, title):
        if title not in self._books:
            raise BookNotFoundError(f"Книга '{title}' не принадлежит библиотеке")
        if not self._books[title]:
            raise BookNotBorrowedError(f"Книга '{title}' не выдавалась")
        self._books[title] = False

