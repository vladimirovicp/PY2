class Date:
    def __init__(self, day: int, month: int, year: int):
        # TODO Инициализируйте переменные с проверкой соответствия типа, если не соответствует, то вызывайте ошибку TypeError
        self.day = day
        self.month = month
        self.year = year

        if not isinstance(self.day, int):
            raise TypeError('Не верный тип дня')

        if not isinstance(self.month, int):
            raise isinstance('Не верный тип месяца')

        if not isinstance(self.year, int):
            raise TypeError('Не верный тип года')

        if  0 > self.day >=31:
            raise ValueError('Не верное число!')





    def __str__(self):
        # TODO Реализуйте возвращение в формате DD/MM/YYYY
        return f"{self.day:0>2}/{self.month:0>2}/{self.year:0>4}"

    def __repr__(self):
        # TODO Реализуйте возвращение в формате Date(day=..., month=..., year=...)
        return f"{self.__class__.__name__}(day={self.day}, month={self.month}, year={self.year})"


if __name__ == "__main__":
    date1 = Date(1, 1, 2021)
    print(date1)  # 01/01/2021
    date2 = Date(11, 10, 1999)
    print(date2)  # 11/10/1999
    print(repr(date1), repr(date2))  # Date(day=1, month=1, year=2021) Date(day=11, month=10, year=1999)

    try:
        Date('1', 1, 2021)
    except TypeError:
        print('Верный вызов TypeError')  # Верный вызов TypeError
    else:
        print('Должен быть вызов TypeError')
