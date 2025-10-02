class Book:
    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.is_reserved = False
        self.is_borrowed = False
        self.reserved_by = None
        self.borrowed_by = None

    def reserve(self, reader):
        if self.is_reserved:
            return False
        if self.is_borrowed:
            return False

        self.is_reserved = True
        self.reserved_by = reader
        return True

    def cancel_reserve(self, reader):
        if not self.is_reserved:
            return False
        if self.reserved_by != reader:
            return False

        self.is_reserved = False
        self.reserved_by = None
        return True

    def get_book(self, reader):
        if self.is_borrowed:
            return False
        if self.is_reserved and self.reserved_by != reader:
            return False

        self.is_borrowed = True
        self.borrowed_by = reader
        self.is_reserved = False
        self.reserved_by = None
        return True

    def return_book(self, reader):
        if not self.is_borrowed:
            return False
        if self.borrowed_by != reader:
            return False

        self.is_borrowed = False
        self.borrowed_by = None
        return True
