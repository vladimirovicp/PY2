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

## task 1.2

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

## task 1.3

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


## task 1.5

doctest — это модуль в стандартной библиотеке Python, который позволяет тестировать фрагменты документации, содержащие примеры кода. Основная цель doctest — обеспечить, чтобы примеры в документации оставались актуальными и работоспособными, выполняя их и проверяя результат.

Зачем нужен doctest?
Проверка корректности документации: Убедиться, что примеры кода в документации действительно работают.
Автоматизация тестирования: Облегчить процесс написания тестов, так как примеры кода можно выполнять и проверять автоматически.
Поддержка кода в актуальном состоянии: Обеспечить, чтобы изменения в коде не ломали примеры в документации.
Как применять doctest?
Использование doctest состоит из нескольких шагов:

Написание примеров в строках документации: Примеры кода вставляются в строку документации функции, метода или класса.
Запуск doctest: Примеры в документации автоматически извлекаются и выполняются модулем doctest.
Важно! doctest проверяет именно корректность тестов, что опишите в документации модуля, функции, класса, метода. Поэтому если тесты пройдены, то ошибок не будет. А если хотя бы один тест не пройден, то будет ошибка, с местом, где тест не пройден.

Работает это таким образом, сначала пишется >>> после этого символа записывается код который выполняется, а ниже прописывается то, с чем нужно сравнить ответ, если ответы совпадают, то всё хорошо, если нет, то напечатается ошибка.

Примеры использования (просто для ознакомления)
Пример 1: Простая функция
Напишем функцию с примерами в строках документации:

```python
def add(a, b):
    """ 
    Возвращает сумму a и b. 
 
    Пример: 
    >>> add(2, 3) 
    5 
    >>> add(-1, 1) 
    0 
    >>> add(0, 0) 
    0 
    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

Пример 2: Класс
Если функция, метод и т.д. ничего не возвращает, то в строке ничего писать не нужно

```python
class Calculator:
    """ 
    Простейший калькулятор. 
 
    Примеры: 
    >>> calc = Calculator()   
    >>> calc.add(2, 3) 
    5 
    >>> calc.subtract(10, 5) 
    5 
    >>> calc.add_no_return(0, 1)  # Здесь ничего не возвращается 
    """

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
    
    def add_no_return(self, a, b):
        a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

Пример 3: Проверка вызова ошибок
doctest позволяет проверить вызов ошибки, для этого необходимо сначала записать Traceback (most recent call last):, а под ним саму ошибку

```python
def divide(a, b):
    """ 
    Делит a на b. 
 
    Пример: 
    >>> divide(6, 3) 
    2.0 
    >>> divide(5, 0) 
    Traceback (most recent call last): 
        ... 
    ZeroDivisionError: division by zero 
    >>> divide(10, 2) 
    5.0 
    """
    return a / b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

Пример 4: Игнорирование частей вывода
Иногда бывает полезно пропустить некоторые части вывода, например, если они изменяются от запуска к запуску (например, адреса памяти). Для этого используется флаг ELLIPSIS:

```python
def foo():
    """ 
    Пример: 
    >>> foo() 
    Some output with ... in the middle 
    """
    print("Some output with dynamic content in the middle")

    
if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
```

Пример 5: Игнорирование пробелов и разрывов строк
Флаг NORMALIZE_WHITESPACE позволяет игнорировать различия в пробелах и разрывах строк между ожидаемым и фактическим выводом:

```python
def bar():
    """ 
    Пример: 
    >>> bar() 
    'text   with   irregular   spacing' 
    """
    return 'text   with   irregular   spacing'

if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
```

Пример 6: Пропуск тестов
Для пропуска теста используется директива # doctest: +SKIP:
```python
def baz():
    """ 
    Пример: 
    >>> baz() # doctest: +SKIP 
    This test will be skipped 
    """
    return "This test will be skipped"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

Пример 7: Запуск doctest из командной строки
Для запуска doctest из командной строки можно использовать следующую команду:

python -m doctest имя_файла.py
Пример 8: Использование doctest в отдельном файле
Иногда удобно писать тесты в отдельном файле. В таком случае можно использовать текстовый файл:

```python
# файл: example.txt
""" 
>>> from mymodule import add 
>>> add(2, 3) 
5 
>>> add(-1, 1) 
0 
>>> add(0, 0) 
0 
"""

if __name__ == "__main__":
    import doctest
    doctest.testfile("example.txt")
```
В документации [doctest](https://docs.python.org/3/library/doctest.html) можно ознакомиться со всем функционалом.

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
        >>> glass = Glass(-500, 0)  # Неверная инициализация класса
        Traceback (most recent call last):
        ...
        ValueError: Объем стакана должен быть положительным числом
        >>> glass = Glass('500', 0)  # Неверная инициализация класса
        Traceback (most recent call last):
        ...
        TypeError: Объем стакана должен быть типа int или float
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

    def is_empty_glass(self) -> bool:
        """
        Функция которая проверяет является ли стакан пустым

        :return: Является ли стакан пустым

        Примеры:
        >>> glass = Glass(500, 0)
        >>> glass.is_empty_glass()
        True
        >>> glass = Glass(500, 100)
        >>> glass.is_empty_glass()
        False
        """
        if self.occupied_volume == 0:
            return True
        return False

    def add_water_to_glass(self, water: float) -> None:
        """
        Добавление воды в стакан.
        :param water: Объем добавляемой жидкости

        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в стакане, то вызываем ошибку

        Примеры:
        >>> glass = Glass(500, 0)
        >>> glass.add_water_to_glass(200)
        >>> glass.occupied_volume
        200
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна положительным числом")
        if self.occupied_volume + water > self.capacity_volume:
            raise ValueError("Перелили жидкость")
        self.occupied_volume += water

    def remove_water_from_glass(self, estimate_water: float) -> None:
        """
        Извлечение воды из стакана.

        :param estimate_water: Объем извлекаемой жидкости
        :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в стакане,
        то возвращается ошибка.

        :return: Объем реально извлеченной жидкости

        Примеры:
        >>> glass = Glass(500, 500)
        >>> glass.remove_water_from_glass(200)
        """
        if not isinstance(estimate_water, (int, float)):
            raise TypeError("Объем извлекаемой жидкости должен быть типа int или float")
        if estimate_water < 0:
            raise ValueError("Объем извлекаемой жидкости должен положительным числом")
        if self.occupied_volume - estimate_water < 0:
            raise ValueError(f"Нельзя извлечь больше, чем есть, на текущий момент есть {self.occupied_volume}")
        self.occupied_volume -= estimate_water


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

```


## task 1.6

Ознакомьтесь с объектно-ориентированной моделью для описания ручки, учитывая различные аспекты и компоненты, из которых она состоит. Это включает в себя:

Чернила(Ink): Цвет и уровень чернил, которые используются при письме.
Стержень(Refill): Компонент, содержащий чернила, и определяющий размер наконечника ручки.
Ручка(Pen): Сам объект ручки, включающий в себя стержень и обладающий функционалом для письма и замены стержня.
Обратите внимание, что при аннотации входных переменных передаются названия классов, это означает, что подразумевается, что будут переданы объекты (экземпляры) данных классов.

Например:

```python
def change_refill(self, new_refill: Refill):
    pass
```
В данном методе подразумевается, что как new_refill передастся объект(экземпляр) класса Refill, на что указывает аннотация.

Создание класса Ink
Этот класс представляет чернила ручки. В него включены следующие атрибуты и методы:

Атрибуты:

color: Цвет чернил (например, синий или черный).
level: Уровень чернил, измеряемый в процентах (от 0 до 100).
Методы:

use(amount): Использует определенное количество чернил. Если уровень чернил становится ниже требуемого, выбрасывается ошибка.
refill(): Полностью заправляет чернила до 100%.
Создание класса Refill
Этот класс представляет стержень ручки. Он включает чернила и информацию о размере наконечника.

Атрибуты:

ink: Объект Ink, представляющий чернила.
tip_size: Размер наконечника в миллиметрах.
Методы:

write(text): Симулирует процесс письма. Рассчитывает количество используемых чернил на основе длины текста и размера наконечника, затем использует эти чернила.
Создание класса Pen
Этот класс представляет саму ручку. Он включает стержень и дополнительные характеристики, такие как бренд и модель.

Атрибуты:

brand: Бренд ручки (например, Parker).
model: Модель ручки.
refill: Объект Refill, представляющий стержень.
Методы:

write(text): Симулирует процесс письма с использованием стержня.
change_refill(new_refill): Заменяет текущий стержень новым.

```python
class Ink:
    def __init__(self, color: str, level: float):
        """
        Инициализация чернил.

        :param color: Цвет чернил.
        :param level: Уровень чернил (в процентах).
        """
        self.color = color
        self.level = level

    def use(self, amount: float):
        """
        Использует определенное количество чернил.

        :param amount: Количество используемых чернил.
        """
        if amount > self.level:
            raise ValueError("Недостаточно чернил для использования.")
        self.level -= amount

    def refill(self):
        """
        Заправка чернил.
        """
        self.level = 100.0
        print("Чернила полностью заправлены")


class Refill:
    def __init__(self, ink: Ink, tip_size: float, consumption: float = 0.1):
        """
        Инициализация стержня.

        :param ink: Объект Ink, представляющий чернила.
        :param tip_size: Размер наконечника (в мм).
        :param consumption: Расход чернил.
        """
        self.ink = ink
        self.tip_size = tip_size
        self.consumption = consumption

    def write(self, text: str):
        """
        Симулирует процесс письма и использует чернила.

        :param text: Текст для написания.
        """
        ink_usage = len(text) * self.tip_size * self.consumption
        self.ink.use(ink_usage)
        print(text)


class Pen:
    def __init__(self, brand: str, model: str, refill: Refill):
        """
        Инициализация ручки.

        :param brand: Бренд ручки.
        :param model: Модель ручки.
        :param refill: Объект Refill, представляющий стержень ручки.
        """
        self.brand = brand
        self.model = model
        self.refill = refill

    def write(self, text: str):
        """
        Симулирует процесс письма с использованием ручки.

        :param text: Текст для написания.
        """
        self.refill.write(text)

    def change_refill(self, new_refill: Refill):
        """
        Замена стержня в ручке.

        :param new_refill: Новый объект Refill для замены.
        """
        self.refill = new_refill


if __name__ == "__main__":
    # Создаем объект Ink
    blue_ink = Ink(color="blue", level=100.0)

    # Создаем объект Refill с чернилами и размером наконечника
    refill = Refill(ink=blue_ink, tip_size=0.5)

    # Создаем объект Pen с брендом, моделью и стержнем
    my_pen = Pen(brand="Parker", model="Jotter", refill=refill)

    # Используем ручку для письма
    print(f"Запас чернил {my_pen.refill.ink.level}")
    my_pen.write("Hello, world!")
    print(f"Запас чернил {my_pen.refill.ink.level}")

    # Заправляем чернила и снова используем ручку
    my_pen.refill.ink.refill()
    print(f"Запас чернил {my_pen.refill.ink.level}")
    my_pen.write("Writing with a newly refilled pen!")
    print(f"Запас чернил {my_pen.refill.ink.level}")

```


## task 1.7

Перед вами классы Монета(Coin), Копилка(PiggyBank).

Необходимо дописать методы add_coin и is_broken класса PiggyBank. Описание классов и методов приведено ниже

Класс Coin: Представляет монету с атрибутом denomination (номинал монеты).

Класс PiggyBank: Представляет копилку с атрибутами coins (список монет) и is_broken (флаг, указывающий, разбита ли копилка).

Метод add_coin: Добавляет монету в копилку, если она не разбита. Если копилка разбита, то вызвать ValueError("Копилка разбита. Нельзя добавить монеты.")

Метод break_piggy_bank: Разбивает копилку, печатает общую сумму монет, возвращает словарь с количеством монет каждого номинала и устанавливает флаг is_broken в True.

В методе break_piggy_bank должен быть реализован следующий функционал:

При вызове метода разбивания копилки печатается общая сумма монет, а также возвращается словарь, где ключ - номинал монеты; значение - количество монет этого номинала. После разбивания копилки атрибут coins с монетами становится пустой. Снова разбить копилку нельзя, должна вызываться ошибка ValueError("Копилка уже разбита.")

```python

class Coin:
    def __init__(self, denomination: float):
        """
        Инициализация монеты.

        :param denomination: Номинал монеты.
        """
        self.denomination = denomination


class PiggyBank:
    def __init__(self):
        """
        Инициализация копилки.
        """
        self.coins = []
        self.is_broken = False

    def add_coin(self, coin: Coin):
        """
        Добавляет монету в копилку.

        :param coin: Объект Coin для добавления.
        """
        if self.is_broken:
            raise ValueError("Копилка разбита. Нельзя добавить монеты.")
        self.coins.append(coin)

    def break_piggy_bank(self):
        """
        Разбивает копилку и возвращает информацию о монетах.

        :return: Словарь, где ключ - номинал монеты, значение - количество монет этого номинала.
        """
        if self.is_broken:
            raise ValueError("Копилка уже разбита.")

        total_amount = sum(coin.denomination for coin in self.coins)
        coin_count = {}

        for coin in self.coins:
            if coin.denomination in coin_count:
                coin_count[coin.denomination] += 1
            else:
                coin_count[coin.denomination] = 1

        self.coins = []
        self.is_broken = True

        print(f"Общая сумма монет: {total_amount}")
        return coin_count


if __name__ == "__main__":
    # Создаем копилку
    piggy_bank = PiggyBank()

    # Создаем несколько монет
    coin1 = Coin(1.0)
    coin2 = Coin(0.5)
    coin3 = Coin(0.25)
    coin4 = Coin(1.0)
    coin5 = Coin(0.5)

    # Добавляем монеты в копилку
    piggy_bank.add_coin(coin1)
    piggy_bank.add_coin(coin2)
    piggy_bank.add_coin(coin3)
    piggy_bank.add_coin(coin4)
    piggy_bank.add_coin(coin5)

    # Печатаем состояние копилки
    print(piggy_bank.coins)

    # Разбиваем копилку
    coins_info = piggy_bank.break_piggy_bank()
    print("Монеты в копилке:", coins_info)

    # Пытаемся добавить монету в разбитую копилку (должна быть ошибка)
    try:
        piggy_bank.add_coin(Coin(2.0))
    except ValueError as e:
        print(e)

    # Пытаемся снова разбить копилку (должна быть ошибка)
    try:
        piggy_bank.break_piggy_bank()
    except ValueError as e:
        print(e)
```
