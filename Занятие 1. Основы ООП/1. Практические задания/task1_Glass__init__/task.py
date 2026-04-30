from typing import Union

class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Класс 'Стакан'
        :param capacity_volume: Объем стакана (вместимость)
        :param occupied_volume: Занятый объём (сколько налили в стакан)
        """

        # TODO создайте атрибут capacity_volume и occupied_volume Обязательно проверяйте типы (TypeError) и значения передаваемых аргументов (ValueError)

        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Не верный тип у capacity_volume")

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Не верный тип у occupied_volume")

        if capacity_volume <= 0:
            raise ValueError('Объем стакана меньше или равен 0')

        if occupied_volume < 0:
            raise  ValueError('Заполненный объем меньше 0')

        if occupied_volume > capacity_volume:
            raise ValueError('Заполненный объем больше чем объем стакана')

        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    # TODO инициализировать два объекта от класса Стакан (Glass)
    glass1 = Glass(100, 50)
    glass2 = Glass(200, 100)

    print(f"Стакан 1: вместимость = {glass1.capacity_volume}, заполнено = {glass1.occupied_volume}")
    print(f"Стакан 2: вместимость = {glass2.capacity_volume}, заполнено = {glass2.occupied_volume}")

    try:
        # TODO инициализировать не корректные объекты
        glass1_1 = Glass(100, 200)
        glass2_2 = Glass(-10, 100)
    except Exception as err:
        print(f"Была вызвана ошибка {err!r}")
    else:
        print("Данный код без ошибок")