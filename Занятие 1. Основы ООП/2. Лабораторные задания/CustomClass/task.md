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
3. Сформировать для каждого класса 2-3 метода, которые будет описывать возможные действия с объектом.
   Если на аргументы накладываются какие-то ограничения, которые в реальной жизни не допустимы,  
   то следует описать валидацию (проверку) этих аргументов. 
    ```python
    class НазваниеКласса:
        ...
    
        def method_1(self):
            ...
    ```
   
4. Каждый метод должен содержать документацию с описанием аргументов(если они есть) и возвращаемого результата(если он есть).
5. Все аргументы методов и возвращаемые результаты должны содержать аннотацию типов.
6. В документации должен содержаться как минимум один [doctest](https://docs.python.org/3/library/doctest.html) пример как пользоваться методом. 


## Пример

<div class="hint">

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

</div>