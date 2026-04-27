class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        # TODO Перепишите под защищенные атрибуты _name, _author
        self.name = name
        self.author = author

    #  TODO Создайте свойство для имени и автора, только для чтения

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:  # TODO Отнаследуйтесь от Book
    def __init__(self, name: str, author: str, pages: int):
        # TODO  Перепишите с учетом наследования атрибутов от родителя
        self.name = name
        self.author = author
        self.pages = pages

    # TODO Напишите свойства для pages с проверками при присвоении им значений

    # TODO Перегрузите метод __repr__


# TODO  Проведите аналогичные необходимые действия согласно заданию для класса AudioBook
class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        self.name = name
        self.author = author
        self.duration = duration
