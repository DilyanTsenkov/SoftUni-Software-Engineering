class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class FirstWordFormatter:
    def format(self, book: Book) -> str:
        for ch in book.content:
            if ch == " ":
                index = book.content.index(" ")
                return book.content[:index]
        return book.content


class Printer:
    def get_book(self, book: Book, formatter):
        return formatter.format(book)


book = Book("daimigo")
print(Printer().get_book(book, Formatter()))
print(Printer().get_book(book, FirstWordFormatter()))
