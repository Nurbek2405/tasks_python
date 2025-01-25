class LibraryBook:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        self.available = False
        return f'Берем книгу...  '

    def return_book(self):
        self.available = True
        return f'Возвращаем книгу...  '

    def show_book(self):
        return f'Книга: {self.title}, Автор: {self.author}, Доступна: {self.available} '

book1 = LibraryBook(1984,'Джордж Оруэл')
print(book1.show_book())
print(book1.borrow())
print(book1.show_book())
print(book1.return_book())
print(book1.show_book())