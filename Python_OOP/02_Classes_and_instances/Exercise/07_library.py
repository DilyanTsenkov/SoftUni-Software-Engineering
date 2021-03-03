class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user):
        if user not in self.user_records:
            self.user_records.append(user)
        return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        self.user_records.remove(user)
        try:
            self.rented_books.pop(user.username)
        except:
            pass

    def change_username(self, user_id: int, new_username: str):
        found = [user_id for u in self.user_records if u.user_id == user_id]
        if not found:
            return f"There is no user with id = {user_id}!"
        for u in self.user_records:
            if u.user_id == found[0]:
                if u.username == new_username:
                    return "Please check again the provided username - it should be different than the username used so far!"
                if u.username in self.rented_books:
                    temp_user_books = self.rented_books[u.username]
                    self.rented_books.pop(u.username)
                    self.rented_books[new_username] = temp_user_books

                u.username = new_username
                return f"Username successfully changed to: {new_username} for userid: {user_id}"


class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        if author in library.books_available:

            if book_name in library.books_available[author]:
                self.books.append(book_name)
                library.books_available[author].remove(book_name)
                if self.username not in library.rented_books:
                    library.rented_books[self.username] = {}
                library.rented_books[self.username][book_name] = days_to_return
                return f"{book_name} successfully rented for the next {days_to_return} days!"

            for u in library.rented_books:
                if book_name in library.rented_books[u]:
                    days_to_return = library.rented_books[u][book_name]
                    return f'The book "{book_name}" is already rented and will be available in {days_to_return} days!'

    def return_book(self, author: str, book_name: str, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"

        self.books.remove(book_name)
        library.books_available[author].append(book_name)
        library.rented_books[self.username].pop(book_name)

    def info(self):
        sorted_books = sorted(self.books)
        if sorted_books:
            return f"{', '.join(sorted_books)}"

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"


user = User(12, 'Peter')
library = Library()
library.add_user(user)
print(library.add_user(user))
library.remove_user(user)
print(library.remove_user(user))
library.add_user(user)
print(library.change_username(2, 'Igor'))
print(library.change_username(12, 'Peter'))
print(library.change_username(12, 'George'))

[print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for user_record in library.user_records]
library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
                                                'The Prisoner of Azkaban',
                                                'The Goblet of Fire',
                                                'The Order of the Phoenix',
                                                'The Half-Blood Prince',
                                                'The Deathly Hallows']})

user.get_book('J.K.Rowling', 'The Deathly Hallows', 17, library)
print(library.books_available)
print(library.rented_books)
print(user.books)
print(user.get_book('J.K.Rowling', 'The Deathly Hallows', 10, library))
print(user.return_book('J.K.Rowling', 'The Cursed Child', library))
user.return_book('J.K.Rowling', 'The Deathly Hallows', library)
print(library.books_available)
print(library.rented_books)
print(user.books)
