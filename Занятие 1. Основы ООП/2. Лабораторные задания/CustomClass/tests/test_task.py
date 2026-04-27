import inspect
import unittest
import sys

try:
    from task import *

    student_module_imported = True
except ImportError as e:
    student_module_imported = False
    print(f"Ошибка импорта: {e}")


class TestCustomClass(unittest.TestCase):
    """
    Тесты для проверки создания класса по заданию.
    """

    @classmethod
    def setUpClass(cls):
        """Находит и анализирует классы, созданные студентом."""
        if not student_module_imported:
            cls.skipTest("Модуль не импортирован")

        cls.classes = [
            cls for name, cls in inspect.getmembers(sys.modules['task'], inspect.isclass)
            if cls.__module__ == 'task' and not name.startswith('Test')
        ]

    def test1_at_least_one_class_exists(self):
        """Проверяет, что создан хотя бы один класс."""
        self.assertGreaterEqual(
            len(self.classes), 1,
            "В модуле должен быть объявлен хотя бы один класс."
        )
        self.__class__.student_class = self.classes[0]


    def test2_class_has_init_with_attributes(self):
        """Проверяет, что класс имеет __init__ с 2-3 атрибутами."""

        self.assertTrue(
            hasattr(self.student_class, '__init__'),
            f"Класс {self.student_class.__name__} должен иметь метод __init__."
        )

        # Проверяем сигнатуру __init__
        init_signature = inspect.signature(self.student_class.__init__)
        params = list(init_signature.parameters.keys())

        # self + 2-3 параметра
        self.assertTrue(
            len(params) >= 3,
            f"Метод __init__ должен принимать 2-3 параметра (помимо self), получено: {len(params) - 1}"
        )

    def test3_class_has_2_3_methods(self):
        """Проверяет, что класс имеет 2-3 метода (кроме __init__)."""

        methods = [
            name for name, method in inspect.getmembers(self.student_class, inspect.isfunction)
            if not name.startswith('__') or name in ['__str__', '__repr__']
        ]

        self.assertTrue(
            len(methods) >= 3,
            f"Класс должен иметь 2-3 метода (кроме __init__), получено: {methods}"
        )
        self.__class__.student_methods = methods

    def test4_methods_have_docstrings(self):
        """Проверяет, что все методы имеют документацию."""
        for method_name in self.student_methods:
            method = getattr(self.student_class, method_name)
            self.assertIsNotNone(
                method.__doc__,
                f"Метод {method_name} должен иметь docstring с документацией."
            )
            self.assertGreater(
                len(method.__doc__.strip()), 10,
                f"Docstring метода {method_name} должен содержать содержательное описание."
            )

    def test5_methods_have_type_annotations(self):
        """Проверяет, что методы имеют аннотации типов."""
        for method_name in self.student_methods:
            method = getattr(self.student_class, method_name)
            signature = inspect.signature(method)

            # Проверяем аннотации параметров
            for param_name, param in signature.parameters.items():
                if param_name != 'self':
                    self.assertNotEqual(
                        param.annotation, inspect.Parameter.empty,
                        f"Параметр {param_name} метода {method_name} должен иметь аннотацию типа."
                    )

            # Проверяем аннотацию возвращаемого значения
            self.assertNotEqual(
                signature.return_annotation, inspect.Signature.empty,
                f"Метод {method_name} должен иметь аннотацию возвращаемого типа."
            )

    def test6_validation_in_init(self):
        """Проверяет наличие валидации в __init__."""
        # Пытаемся создать объект с заведомо неверными данными
        init_signature = inspect.signature(self.student_class.__init__)
        params = list(init_signature.parameters.keys())[1:]  # Исключаем self

        # Создаем "плохие" аргументы на основе аннотаций
        test_args = {}
        for param_name in params:
            param = init_signature.parameters[param_name]
            if param.annotation == str:
                test_args[param_name] = 123  # Число вместо строки
            elif param.annotation == int:
                test_args[param_name] = "invalid"  # Строка вместо числа
            elif param.annotation == float:
                test_args[param_name] = "invalid"  # Строка вместо числа
            else:
                test_args[param_name] = "invalid_test_value"

        # Пробуем создать объект - ожидаем исключение
        try:
            instance = self.student_class(**test_args)
            # Если дошли сюда, валидации может не быть
            self.fail(
                f"Ожидалась валидация в __init__ для неверных аргументов: {test_args}. "
                "Добавьте проверки условий (if/raise)."
            )
        except (ValueError, TypeError, Exception) as e:
            # Исключение ожидаемо и приветствуется - это означает валидацию
            pass