# TODO скопириуйте и запустите здесь необходимый код

class Parent:
    public_class_attr = 0
    _protected_class_attr = 1
    __private_class_attr = 2

    def __init__(self):
        self.public_attr = 3
        self._protected_attr = 4
        self.__private_attr = 5


class Child(Parent):
    def get_public_class_attr(self):
        return self.public_class_attr

    def get_protected_class_attr(self):
        return self._protected_class_attr

    def get_private_class_attr(self):
        return self.__private_class_attr

    def get_public_attr(self):
        return self.public_attr

    def get_protected_attr(self):
        return self._protected_attr

    def get_private_attr(self):
        return self.__private_attr


if __name__ == "__main__":
    child = Child()

    print(child.get_public_class_attr())  # 0
    print(child.get_protected_class_attr())  # 1

    try:
        print(child.get_private_class_attr())
    except AttributeError as err:
        print(err)  # 'Child' object has no attribute '_Child__private_class_attr'

    print(child.get_public_attr())  # 3
    print(child.get_protected_attr())  # 4

    try:
        print(child.get_private_attr())
    except AttributeError as err:
        print(err)  # 'Child' object has no attribute '_Child__private_attr'
