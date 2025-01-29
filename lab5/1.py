class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self) -> None:
        print(f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}")

newBook = Book("Девственность", "Евгений Алехин", 2022)
newBook.get_info()