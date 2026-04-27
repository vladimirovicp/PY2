from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Класс 'Стакан'
        :param capacity_volume: Объем стакана (вместимость)
        :param occupied_volume: Занятый объём (сколько налили в стакан)
        """

        # TODO создайте атрибут capacity_volume и occupied_volume Обязательно проверяйте типы (TypeError) и значения передаваемых аргументов (ValueError)


if __name__ == "__main__":
    # TODO инициализировать два объекта от класса Стакан (Glass)

    try:
        ...  # TODO инициализировать не корректные объекты
    except Exception as err:
        print(f"Была вызвана ошибка {err!r}")
    else:
        print("Данный код без ошибок")


