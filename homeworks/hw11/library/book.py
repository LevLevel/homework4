class Book:
    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.is_reserved = False
        self.is_borrowed = False
        self.current_user = None

    def reserve(self, reader):
        if self.is_reserved or self.is_borrowed:
            return False

        self.is_reserved = True
        self.current_user = reader
        return True

    def cancel_reserve(self, reader):
        if not self.is_reserved or self.current_user != reader:
            return False

        self.is_reserved = False
        self.current_user = None
        return True

    def get_book(self, reader):
        if self.is_borrowed or (self.is_reserved and self.current_user != reader):
            return False

        self.is_borrowed = True
        self.is_reserved = False
        self.current_user = reader
        return True

    def return_book(self, reader):
        if not self.is_borrowed or self.current_user != reader:
            return False

        self.is_borrowed = False
        self.current_user = None
        return True
