import json
from datetime import datetime


class Task:
    """Класс, представляющий задачу."""

    def __init__(self, title: str, description: str = "") -> None:
        """
        Инициализирует новую задачу.

        Args:
            title: Название задачи (не может быть пустым).
            description: Описание задачи (опционально).

        Raises:
            ValueError: Если название пустое.
        """
        ...  # TODO Реализуйте проверку, что title не пустое

        ...  # TODO Создайте атрибут title и description
        ...  # TODO Создайте атрибуты is_done и created_at

    def mark_as_done(self) -> None:
        """Отмечает задачу как выполненную."""
        ... # TODO Отметьте задачу как выполненную, используйте атрибут is_done и переведите его в True

    def __str__(self) -> str:
        """Возвращает строковое представление задачи."""
        return ''  # TODO Реализуйте понятный вывод статуса задачи

    def to_dict(self) -> dict:
        """
        Преобразует задачу в словарь для сохранения.

        Returns:
            Словарь с данными задачи.
        """
        return {
            "title": self.title,
            "description": self.description,
            "is_done": self.is_done,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Task':
        """
        Создает задачу из словаря. Возвращает объект класса Task

        Args:
            data: Словарь с данными задачи.

        Returns:
            Объект Task.
        """
        task = cls(data["title"], data["description"])
        task.is_done = data["is_done"]
        task.created_at = datetime.fromisoformat(data["created_at"])
        return task


class TodoList:
    """Класс для управления списком задач с сохранением в файл."""

    def __init__(self, filename: str = "tasks.json") -> None:
        """
        Инициализирует менеджер задач.

        Args:
            filename: Имя файла для сохранения задач.
        """
        ...  # TODO Создайте атрибут filename со значением имени файла для сохранения
        ...  # TODO Создайте атрибут tasks с пустым списком
        ...  # TODO Вызовите метод load_from_file для загрузки данных с файла

    def save_to_file(self) -> None:
        """Сохраняет все задачи в файл JSON."""
        ...  # TODO Реализуйте код по сохранению задач в файл формата json с названием файла из атрибута filename

    def load_from_file(self) -> None:
        """Загружает задачи из файла JSON."""
        ...  # TODO Реализуйте код загрузки данных с файла. Помните, что файла может не существовать

    def add_task(self, task: Task) -> None:
        """
        Добавляет задачу в список и сохраняет в файл.

        Args:
            task: Объект задачи для добавления.
        """
        ... # TODO Реализуйте код

    def list_tasks(self) -> None:
        """Выводит все задачи с их порядковыми номерами (начиная с 1).
        Если задач нет, то выводит сообщение 'Список задач пуст!'"""
        ... # TODO Реализуйте код

    def mark_task_done(self, index: int) -> None:
        """
        Отмечает задачу как выполненную. Сохраняет изменения в файл.

        Args:
            index: Номер задачи в списке (начиная с 1).

        Raises:
            IndexError: Если номер задачи неверный.
        """
        ... # TODO Реализуйте код

    def remove_task(self, index: int) -> None:
        """
        Удаляет задачу из списка. Сохраняет изменения в файл.

        Args:
            index: Номер задачи в списке (начиная с 1).

        Raises:
            IndexError: Если номер задачи неверный.
        """
        ... # TODO Реализуйте код


def main():
    """Функция логики работы приложения"""
    todo = TodoList()  # Объект менеджера задач

    while True:
        print("\n=== Менеджер задач ===")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Отметить задачу выполненной")
        print("4. Удалить задачу")
        print("5. Выйти")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            todo.list_tasks()
        elif choice == "2":  # Добавить задачу
            title = input("Введите название задачи: ")
            description = input("Введите описание (не обязательно): ")
            ... # TODO Реализуйте логику добавления объекта задачи в объект todo (объект менеджера задач)
        elif choice == "3":  # Отметить задачу выполненной
            ...  # TODO Реализуйте функционал
        elif choice == "4":  # Удалить задачу
            ...  # TODO Реализуйте функционал
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()  # Проверьте работоспособность приложения