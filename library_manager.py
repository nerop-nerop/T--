import json
from book import Book

class LibraryManager:
    def __init__(self, data_file="library_data.json"):
        self.data_file = data_file
        self.books = self.load_books()

    def load_books(self):
        """Загружает книги из JSON файла."""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Book.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return [] 