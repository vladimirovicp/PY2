class Book:
    def __init__(self, id_, name, pages):
        pass  # TODO Инициализировать экземплярные атрибуты (не забываем что они создаются с использованием self)

    def __str__(self):
        pass  # TODO Вернуть строку типа "Книга 'название книги'"

    def __repr__(self):
        pass  # TODO Вернуть строку представления объекта типа Book(id_=1, name='test_name_1', pages=200)


if __name__ == '__main__':
    # База данных книг для проверки
    BOOKS_DATABASE = [
        {
            "id": 1,
            "name": "test_name_1",
            "pages": 200,
        },
        {
            "id": 2,
            "name": "test_name_2",
            "pages": 400,
        }
    ]

    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
