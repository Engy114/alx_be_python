# library_management.py

class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author):
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Check out the book, marking it as unavailable."""
        if self._is_checked_out:
            return False  # Book is already checked out
        self._is_checked_out = True
        return True

    def return_book(self):
        """Return the book, making it available again."""
        if not self._is_checked_out:
            return False  # Book is already available
        self._is_checked_out = False
        return True

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """A class representing a collection of books in the library."""

    def __init__(self):
        self._books = []  # Private list to store books

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False  # Book not found

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False  # Book not found

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [f"{book.title} by {book.author}" for book in self._books if book.is_available()]
        if available_books:
            print("\n".join(available_books))
        else:
            print("No available books.")
