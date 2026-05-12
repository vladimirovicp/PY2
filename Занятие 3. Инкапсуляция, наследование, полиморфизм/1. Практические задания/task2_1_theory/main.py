# TODO скопириуйте и запустите здесь необходимый код


class A:
    class_attr = 10  # классовый атрибут

    def __init__(self, param):
        self.param = param  # экземплярный атрибут

    @classmethod
    def change_class_attr(cls, value):
        cls.class_attr = value

    def get_param(self):  # экземплярный метод
        return self.param


class B(A):  # В классе мы прописываем, то что хотим добавить относительно родительского класса A
    new_attr = 'Это классовый атрибут класса B'

    @staticmethod
    def hello():  # Добавили метод которого не было в классе A
        print("Привет из класса B")


if __name__ == "__main__":
    obj_a = A(20)
    obj_b = B(40)

    print(obj_b.class_attr)  # 10 Есть атрибут скопированный из класса А
    print(obj_b.new_attr)  # 'Это классовый атрибут класса B' и новый атрибут которого нет в классе A

    print(obj_b.get_param())  # 40 Есть метод скопированный из класса А
    obj_b.hello()  # "Привет из класса B" и новый метод которого нет в классе A