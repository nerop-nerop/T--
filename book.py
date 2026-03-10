import uuid

class Book:
    def __init__(self, title, author, genre, year, description, book_id=None, is_read=False, is_favorite=False):
        self.id = book_id if book_id else str(uuid.uuid4()) 