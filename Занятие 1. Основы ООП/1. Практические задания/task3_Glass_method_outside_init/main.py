from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        #  TODO заменить на метод init_capacity_volume как в примере (не забываем что начальное значение None)
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume  # объем стакана

        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)

    # TODO создать метод init_capacity_volume, который будет инициализировать атрибут capacity_volume

    def init_occupied_volume(self, occupied_volume):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume  # объем жидкости в стакане


if __name__ == "__main__":
    glass = ...  # TODO инициализировать экземпляр класса Glass с объемом 200 и количеством жидкости 100

    print(...)  # TODO распечатать атрибут capacity_volume
    print(...)  # TODO распечатать атрибут occupied_volume
