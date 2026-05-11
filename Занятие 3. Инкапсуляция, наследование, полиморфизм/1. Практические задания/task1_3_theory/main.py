# TODO скопириуйте и запустите здесь необходимый код
class Rectangle:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    def get_width(self) -> float:
        """Метод для получения ширины"""
        return self._width

    def set_width(self, value: float):
        """Метод для установки ширины с проверкой"""
        if value <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        self._width = value

    def get_height(self) -> float:
        """Метод для получения высоты"""
        return self._height

    def set_height(self, value: float):
        """Метод для установки высоты с проверкой"""
        if value <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self._height = value

    def area(self) -> float:
        """Вычисляемый метод для площади прямоугольника"""
        return self._width * self._height

if __name__ == "__main__":

    # Пример использования
    rect = Rectangle(5, 10)

    print(rect.get_width())  # 5
    rect.set_width(7)
    print(rect.area())  # 70

    try:
        rect.set_width(-3)  # Ошибка: ValueError: Ширина должна быть положительным числом
    except ValueError as err:
        print(repr(err))
