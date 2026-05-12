class Counter:
    def __init__(self, max_value: int):
        self._value = 0
        self._max_value = max_value

    def increment(self) -> None:
        if self._value < self._max_value:
            self._value += 1
        else:
            self._value = 0

    # TODO перепишите get_value и сделайте его свойством (getter) value
    @property
    def value(self) -> int:
        return self._value

    # TODO  напишите свойство (getter) max_value
    @property
    def max_value(self):
        return self._max_value

    # TODO  напишите свойство (setter) max_value с проверками на входной тип и значение

    @max_value.setter
    def max_value(self, max_val: int):
        if not isinstance(max_val, int):
            raise TypeError('Не верный тип max_value')

        if max_val < 1:
            raise ValueError('max_value меньше одного')

        self._max_value = max_val


if __name__ == "__main__":
    counter = Counter(5)

    counter.max_value = 3

    for _ in range(4):
        counter.increment()
        print(f"Counter value: {counter.value}")

    try:
        counter.value = 4
    except AttributeError as err:
        print(err)  # property 'value' of 'Counter' object has no setter
