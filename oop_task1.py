class Book :
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def show_book(self):
        return print(f' Книга: {self.title}, Автор: {self.author}, Год: {self.year} ')

book1 = Book ('Гарри Поттер','Джоан Роулинг',2001)
book2 = Book ('1984','Джордж Оруэлл',1949)

book1.show_book()
book2.show_book()

print(type(book1))
