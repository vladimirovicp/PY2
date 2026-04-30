# CustomClass

1. Придумать и написать один класс, описывающий любой объект.
Например, в качестве объектов могут выступать материальные сущности стол, дерево, и даже нематериальные стек, Facebook.

```python
class НазваниеКласса:
    ...
```
2. Для каждого класса выделить 2-3 характеристики и записать их в виде атрибутов.
Если на аргументы конструктора накладываются какие-то ограничения, которые в реальной жизни не допустимы,
то следует описать валидацию (проверку) этих аргументов.

```python
class НазваниеКласса:
    def __init__(self, arg1, arg2):
        # Атрибутам присваиваются значения аргументов конструктора объекта
        self.attr1 = arg1
        self.attr2 = arg2
```

3. Сформировать для каждого класса 2-3 метода, которые будет описывать возможные действия с объектом. Если на аргументы накладываются какие-то ограничения, которые в реальной жизни не допустимы,
то следует описать валидацию (проверку) этих аргументов.
```python
class НазваниеКласса:
    ...

    def method_1(self):
        ...
```

4. Каждый метод должен содержать документацию с описанием аргументов(если они есть) и возвращаемого результата(если он есть).

5. Все аргументы методов и возвращаемые результаты должны содержать аннотацию типов.

6. В документации должен содержаться как минимум один doctest пример как пользоваться методом.

## Пример

```python
import doctest

class Glass:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """ 
        Создание и подготовка к работе объекта "Стакан" 
 
        :param capacity_volume: Объем стакана 
        :param occupied_volume: Объем занимаемой жидкости 
 
        Примеры: 
        >>> glass = Glass(500, 0)  # инициализация экземпляра класса 
        >>> glass.occupied_volume, glass.capacity_volume 
        (0, 500) 
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем стакана должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем стакана должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty(self) -> bool:
        """ 
        Функция которая проверяет является ли стакан пустым 
 
        :return: Является ли стакан пустым 
 
        Примеры: 
        >>> glass = Glass(500, 0) 
        >>> glass.is_empty() 
        True 
        """
        if self.occupied_volume == 0:
            return True
        return False

    def add_water(self, water: float) -> None:
        """ 
        Добавление воды в стакан. 
        :param water: Объем добавляемой жидкости 
 
        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в стакане, то вызываем ошибку 
 
        Примеры: 
        >>> glass = Glass(500, 0) 
        >>> glass.add_water(200) 
        >>> glass.occupied_volume 
        200 
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if not 0 < water <= self.capacity_volume - self.occupied_volume:
            raise ValueError("Добавляемая жидкость должна положительным числом и не перелить через край")
        self.occupied_volume += water

    def remove_water(self, water: float) -> None:
        """ 
        Извлечение воды из стакана. 
 
        :param water: Объем извлекаемой жидкости 
        :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в стакане, 
        то возвращается ошибка. 
 
        :return: Объем реально извлеченной жидкости 
 
        Примеры: 
        >>> glass = Glass(500, 500) 
        >>> glass.remove_water(200) 
        >>> glass.occupied_volume 
        300 
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Убираемый объем жидкости должен быть типа int или float")
        if not 0 < water <= self.occupied_volume:
            raise ValueError("Убираемый объем жидкости должен быть положительным числом и не более занятого объема")
        self.occupied_volume -= water

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

```


## Решение

```python
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
```