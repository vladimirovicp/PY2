import doctest

"""
### Требования:

1. **Класс должен иметь конструктор `__init__`** с 2-3 параметрами, которые сохраняются в атрибуты объекта
2. **Реализовать валидацию** входных данных в конструкторе (проверка на допустимые значения)
3. **Добавить 2-3 метода** для описания поведения объекта
4. **Каждый метод должен иметь**:
   - Docstring с описанием параметров и возвращаемого значения
   - Аннотации типов для всех параметров и возвращаемого значения
5. **Реализовать валидацию** входных данных в методах (где это необходимо)
"""

# TODO Создайте свой класс по заданию

# В качестве объекта выбран Рюкзак (Backpack).

import doctest


class Backpack:
    def __init__(self, capacity: float, current_load: float = 0.0, is_zipped: bool = False):
        """
        Создание и подготовка к работе объекта "Рюкзак"

        :param capacity: Максимальная вместимость рюкзака в литрах
        :param current_load: Текущая загруженность в литрах
        :param is_zipped: Состояние молнии (застегнут/расстегнут)

        Примеры:
        >>> bp = Backpack(40, 5.0)
        >>> bp.capacity, bp.current_load, bp.is_zipped
        (40, 5.0, False)
        """
        if not isinstance(capacity, (int, float)):
            raise TypeError("Вместимость должна быть числом (int или float)")
        if capacity <= 0:
            raise ValueError("Вместимость рюкзака должна быть положительным числом")
        self.capacity = float(capacity)

        if not isinstance(current_load, (int, float)):
            raise TypeError("Текущая загрузка должна быть числом (int или float)")
        if current_load < 0:
            raise ValueError("Текущая загрузка не может быть отрицательной")
        if current_load > self.capacity:
            raise ValueError("Начальная загрузка не может превышать вместимость рюкзака")
        self.current_load = float(current_load)

        if not isinstance(is_zipped, bool):
            raise TypeError("Состояние молнии должно быть булевым значением (bool)")
        self.is_zipped = is_zipped

    def pack_item(self, volume: float) -> None:
        """
        Добавляет предмет в рюкзак.

        :param volume: Объем добавляемого предмета в литрах
        :raise ValueError: Если рюкзак застегнут, объем отрицательный или предмет не помещается
        :raise TypeError: Если volume не является числом
        :return: None

        Примеры:
        >>> bp = Backpack(50, 10.0)
        >>> bp.pack_item(15.0)
        >>> bp.current_load
        25.0
        """
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем предмета должен быть числом (int или float)")
        if volume <= 0:
            raise ValueError("Объем предмета должен быть положительным числом")
        if self.is_zipped:
            raise ValueError("Рюкзак застегнут. Расстегните молнию перед добавлением предметов")
        if self.current_load + volume > self.capacity:
            raise ValueError("Предмет не помещается в рюкзак")
        self.current_load += volume

    def unpack_item(self, volume: float) -> None:
        """
        Извлекает предмет из рюкзака.

        :param volume: Объем извлекаемого предмета в литрах
        :raise ValueError: Если рюкзак застегнут, объем отрицательный или превышает текущую загрузку
        :raise TypeError: Если volume не является числом
        :return: None

        Примеры:
        >>> bp = Backpack(50, 25.0)
        >>> bp.unpack_item(10.0)
        >>> bp.current_load
        15.0
        """
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем предмета должен быть числом (int или float)")
        if volume <= 0:
            raise ValueError("Объем извлекаемого предмета должен быть положительным числом")
        if self.is_zipped:
            raise ValueError("Рюкзак застегнут. Расстегните молнию перед извлечением предметов")
        if volume > self.current_load:
            raise ValueError("Нельзя извлечь больше, чем лежит в рюкзаке")
        self.current_load -= volume

    def toggle_zip(self) -> None:
        """
        Переключает состояние молнии (застегивает или расстегивает).

        :return: None

        Примеры:
        >>> bp = Backpack(30, 5.0, is_zipped=False)
        >>> bp.toggle_zip()
        >>> bp.is_zipped
        True
        >>> bp.toggle_zip()
        >>> bp.is_zipped
        False
        """
        self.is_zipped = not self.is_zipped


if __name__ == "__main__":
    # Запускает автоматическую проверку всех примеров из docstring'ов
    doctest.testmod()