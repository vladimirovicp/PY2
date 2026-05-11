# TODO скопириуйте и запустите здесь необходимый код
class MyClass:
    def __init__(self, value):
        self.__value = value  # Приватный атрибут

    def __my_method(self):  # Приватный метод
        return self.__value

if __name__ == "__main__":
    obj = MyClass(42)
    # print(obj.__value)  # Ошибка, доступ невозможен напрямую
    # obj.__my_method()   # Ошибка, доступ невозможен напрямую

    # Однако, есть обходной путь (механизм манглинга):
    print(obj._MyClass__value)  # Доступ возможен через манглинг имен, но это очень не рекомендуется
