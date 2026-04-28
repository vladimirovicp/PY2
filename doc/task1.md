# Основы ООП

Экземплярные атрибуты capacity_volume и occupied_volume в классе Glass. Экземплярные атрибуты создаются в методе __init__
При создании атрибутов обязательно проверьте типы capacity_volume и occupied_volume в случае несоответствия вызовите (TypeError), а также проверьте значения передаваемых аргументов, и в случае несоответствия:

Объем стакана меньше или равен 0
Заполненный объем меньше 0
Заполненный объем больше чем объем стакана
вызовите ошибку ValueError

Создайте два объекта от класса Glass.

Попробуйте инициализировать объекты с некорректными типами и значениями аргументов.

```python
from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Класс 'Стакан'
        :param capacity_volume: Объем стакана (вместимость)
        :param occupied_volume: Занятый объём (сколько налили в стакан)
        """

        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Тип должен быть или int или float")
        if not capacity_volume > 0:
            raise ValueError("Объем стакана должен быть больше 0")
        self.capacity_volume = capacity_volume  # объем стакана

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Тип должен быть или int или float")
        if occupied_volume < 0:
            raise ValueError("Не должно быть отрицательных значений")
        if occupied_volume > capacity_volume:
            raise ValueError("Налить в стакан больше того, что возможно нельзя")

        self.occupied_volume = occupied_volume  # объем жидкости в стакане


if __name__ == "__main__":
    glass1 = Glass(200, 100)
    glass2 = Glass(200, 150)

    try:
        Glass(-200, 100)
    except Exception as err:
        print(f"Была вызвана ошибка {err!r}")
    else:
        print("Данный код без ошибок")
```

## task 2

1. Создайте два объекта типа Glass.
2. Измените и добавьте во второй стакан любое кол-во воды (через соответствующий атрибут). Убедитесь, что у других объектов Glass атрибуты экземпляра класса не изменились.
3. С помощью оператора is убедитесь, что glass1 и glass2 это разные объекты.


```python
from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Класс 'Стакан'
        :param capacity_volume: Объем стакана (вместимость)
        :param occupied_volume: Занятый объём (сколько налили в стакан)
        """

        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Тип должен быть или int или float")
        if not capacity_volume > 0:
            raise ValueError("Объем стакана должен быть больше 0")
        self.capacity_volume = capacity_volume  # объем стакана

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Тип должен быть или int или float")
        if occupied_volume < 0:
            raise ValueError("Не должно быть отрицательных значений")
        if occupied_volume > capacity_volume:
            raise ValueError("Налить в стакан больше того, что возможно нельзя")

        self.occupied_volume = occupied_volume  # объем жидкости в стакане


if __name__ == "__main__":
    glass1 = Glass(200, 100)  # экземпляр класса
    print(glass1.capacity_volume, glass1.occupied_volume)

    glass2 = Glass(200, 150)
    print(glass2.capacity_volume, glass2.occupied_volume)

    print("Доливаем воды в первый стакан...")
    glass1.occupied_volume += 50

    print(glass1.capacity_volume, glass1.occupied_volume)
    print(glass2.capacity_volume, glass2.occupied_volume)

    assert glass1.capacity_volume == glass2.capacity_volume  # Проверяем, что объемы стаканов одинаковые (иначе будет ошибка)
    assert glass1.occupied_volume == glass2.occupied_volume  # Проверяем, что стаканы заполнены одинаково (иначе будет ошибка)

    print(id(glass1) == id(glass2))  # TODO сравнить id объектов (должно вернуть True или False)

```

## task 3

1. Вынесите инициализацию атрибута capacity_volume в отдельный метод init_capacity_volume.
Для этого необходимо установить первоначальное значение атрибуту, например None, и вызвать метод,
который будет инициализировать этот атрибут.

from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)

        ...
2. Самостоятельно инициализировать экземпляр класса Glass с объемом 200 и количеством жидкости 100.
3. Распечатать атрибуты экземпляр класса Glass capacity_volume и occupied_volume