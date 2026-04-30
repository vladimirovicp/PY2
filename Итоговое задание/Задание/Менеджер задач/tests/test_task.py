import unittest
import os
import json
import tempfile
from task import Task, TodoList


class TestTodoList(unittest.TestCase):
    """Тесты для менеджера задач."""

    def setUp(self):
        # Создаем временный файл для тестов
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        self.filename = self.temp_file.name

    def tearDown(self):
        # Удаляем временный файл после теста
        if os.path.exists(self.filename):
            os.unlink(self.filename)

    def test1_task_creation_validation(self):
        """Тест: нельзя создать задачу с пустым названием."""
        with self.assertRaises(ValueError):
            Task("")

    def test2_task_mark_as_done(self):
        """Тест: отметка задачи как выполненной."""
        task = Task("Тестовая задача")
        self.assertFalse(task.is_done)
        task.mark_as_done()
        self.assertTrue(task.is_done)

    def test3_task_to_dict_and_back(self):
        """Тест: преобразование задачи в словарь и обратно."""
        original_task = Task("Тест", "Описание")
        original_task.mark_as_done()

        # В словарь и обратно
        task_dict = original_task.to_dict()
        restored_task = Task.from_dict(task_dict)

        self.assertEqual(original_task.title, restored_task.title)
        self.assertEqual(original_task.description, restored_task.description)
        self.assertEqual(original_task.is_done, restored_task.is_done)

    def test4_todo_list_add_and_save(self):
        """Тест: добавление задачи и сохранение в файл."""
        todo = TodoList(self.filename)
        task = Task("Новая задача")

        todo.add_task(task)

        # Проверяем, что файл создался и содержит данные
        self.assertTrue(os.path.exists(self.filename))

        with open(self.filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]['title'], "Новая задача")

    def test5_todo_list_load_from_file(self):
        """Тест: загрузка задач из файла."""
        # Сначала создаем и сохраняем задачи
        original_todo = TodoList(self.filename)
        original_todo.add_task(Task("Задача 1"))
        original_todo.add_task(Task("Задача 2"))

        # Теперь загружаем в новый объект
        new_todo = TodoList(self.filename)

        self.assertEqual(len(new_todo.tasks), 2)
        self.assertEqual(new_todo.tasks[0].title, "Задача 1")
        self.assertEqual(new_todo.tasks[1].title, "Задача 2")

    def test6_todo_list_mark_done_and_save(self):
        """Тест: отметка задачи как выполненной и проверка сохранения."""
        todo = TodoList(self.filename)
        todo.add_task(Task("Тестовая задача"))

        # Отмечаем как выполненную
        todo.mark_task_done(1)

        # Загружаем заново и проверяем
        new_todo = TodoList(self.filename)
        self.assertTrue(new_todo.tasks[0].is_done)

    def test7_todo_list_remove_task(self):
        """Тест: удаление задачи."""
        todo = TodoList(self.filename)
        todo.add_task(Task("Задача 1"))
        todo.add_task(Task("Задача 2"))

        self.assertEqual(len(todo.tasks), 2)
        todo.remove_task(1)
        self.assertEqual(len(todo.tasks), 1)
        self.assertEqual(todo.tasks[0].title, "Задача 2")

    def test8_invalid_task_index(self):
        """Тест: обработка неверного номера задачи."""
        todo = TodoList(self.filename)
        todo.add_task(Task("Задача 1"))

        with self.assertRaises(IndexError):
            todo.mark_task_done(999)  # Несуществующий номер

        with self.assertRaises(IndexError):
            todo.remove_task(0)  # Неверный номер