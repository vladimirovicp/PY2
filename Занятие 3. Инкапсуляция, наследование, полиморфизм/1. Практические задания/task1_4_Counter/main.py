class Counter:
    def __init__(self, max_value: int):
        self._value = 0
        self._max_value = max_value

    def increment(self) -> None:
        # TODO допишите метод
        if self._max_value <= self._value:
            self._value = 0
        else:
            self._value += 1


    def get_value(self) -> int:
        return self._value # TODO допишите метод


if __name__ == "__main__":
    counter = Counter(5)

    for _ in range(7):
        counter.increment()
        print(f"Counter value: {counter.get_value()}")
