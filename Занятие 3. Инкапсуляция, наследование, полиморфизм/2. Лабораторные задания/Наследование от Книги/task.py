class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        # TODO Перепишите под защищенные атрибуты _name, _author

        self.__validate_name(name)
        self._name = name
        self.__validate_author(author)
        self._author = author

    @staticmethod
    def __validate_name(name: str):
        """
        Проверка на соответствие типу str, иначе ошибка TypeError
        """
        if not isinstance(name, str):
            raise TypeError()

    @property
    def name(self):
        return self._name

    @staticmethod
    def __validate_author(author: str):
        """
        Проверка на соответствие типу str, иначе ошибка TypeError
        """
        if not isinstance(author, str):
            raise TypeError()

    @property
    def author(self):
        return self._name


    #  TODO Создайте свойство для имени и автора, только для чтения

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):  # TODO Отнаследуйтесь от Book
    def __init__(self, name: str, author: str, pages: int):
        # TODO  Перепишите с учетом наследования атрибутов от родителя
        super().__init__(name, author)
        # self.name = name
        # self.author = author
        self.__validate_pages(pages)
        self.__pages = pages

    @staticmethod
    def __validate_pages(pages: int):
        """
        Проверка на соответствие типу float, иначе ошибка TypeError
        """
        if not isinstance(pages, int):
            raise TypeError()

        if pages <= 0:
            raise ValueError("Количество страниц не может быть меньше 0")

    @property
    def pages(self):
        return self.__pages

    # TODO Напишите свойства для pages с проверками при присвоении им значений
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"



    # TODO Перегрузите метод __repr__
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


# TODO  Проведите аналогичные необходимые действия согласно заданию для класса AudioBook
class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        # self.name = name
        # self.author = author
        self.__validate_duration(duration)
        self.__duration = duration


    @staticmethod
    def __validate_duration(duration: float):
        """
        Проверка на соответствие типу float, иначе ошибка TypeError
        """
        if not isinstance(duration, float):
            raise TypeError()

        if duration <= 0:
            raise ValueError("Продолжительность не может быть меньше 0")

    @property
    def duration(self):
        return self.__duration

    # TODO Напишите свойства для pages с проверками при присвоении им значений
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    # TODO Перегрузите метод __repr__
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
