from library_manager import LibraryManager

def display_menu():
    """Отображает главное меню приложения."""
    print("\n--- T-Библиотека ---")
    print("1. Добавить книгу")
    print("2. Просмотреть все книги")
    print("3. Найти книгу (по ID)")
    print("4. Удалить книгу")
    print("5. Отметить книгу как прочитанную/не прочитанную")
    print("6. Добавить/удалить книгу из избранного")
    print("7. Просмотреть избранные книги")
    print("8. Поиск книг по ключевому слову")
    print("9. Сортировать книги")
    print("10. Фильтровать книги")
    print("0. Выход")
    print("--------------------")

def get_book_details_from_user():
    """Получает информацию о книге от пользователя."""
    title = input("Введите название книги: ")
    author = input("Введите автора: ")
    genre = input("Введите жанр: ")
    while True:
        try:
            year = int(input("Введите год издания: "))
            break
        except ValueError:
            print("Ошибка: Введите корректный год (число).")
    description = input("Введите краткое описание: ")
    return title, author, genre, year, description

def display_books(books):
    """Отображает список книг."""
    if not books:
        print("В библиотеке пока нет книг.")
        return
    print("\n--- Список книг ---")
    for i, book in enumerate(books):
        