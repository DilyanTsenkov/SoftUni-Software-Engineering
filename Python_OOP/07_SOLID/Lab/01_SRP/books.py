class Library:
    def __init__(self, name, books, location):
        self.name = name
        self.books = books
        self.location = location

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book

            
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class BookReader:
    def __init__(self, book):
        self.book = book
        self.page = 0

    def current_page(self, page):
        self.page = page
