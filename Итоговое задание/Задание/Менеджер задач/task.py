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
        # TODO Реализуйте проверку, что title не пустое

        if not title:
            raise ValueError("title пустое")

        # TODO Создайте атрибут title и description
        self.title = title # название
        self.description = description # описание

        # TODO Создайте атрибуты is_done и created_at
        self.is_done = False # булево значение (по умолчанию False)
        self.created_at = datetime.now() #дата создания

    def mark_as_done(self) -> None:
        """Отмечает задачу как выполненную."""
        # TODO Отметьте задачу как выполненную, используйте атрибут is_done и переведите его в True
        self.is_done = True
    def __str__(self) -> str:
        """Возвращает строковое представление задачи."""
        status = "[X]" if self.is_done else '[ ]'
        return f"{status} {self.title}"  # TODO Реализуйте понятный вывод статуса задачи

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
        self.filename = filename  # TODO Создайте атрибут filename со значением имени файла для сохранения
        self.tasks = []  # TODO Создайте атрибут tasks с пустым списком
        self.load_from_file()  # TODO Вызовите метод load_from_file для загрузки данных с файла

    def save_to_file(self) -> None:
        """Сохраняет все задачи в файл JSON."""
          # TODO Реализуйте код по сохранению задач в файл формата json с названием файла из атрибута filename
        try:
            tasks_data = [task.to_dict() for task in self.tasks]

            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(tasks_data, file, ensure_ascii=False, indent=2)

            print(f"✅ Задачи сохранены в файл '{self.filename}'")
        except Exception as e:
            print(f"❌ Ошибка при сохранении файла: {e}")

    def load_from_file(self) -> None:
        """Загружает задачи из файла JSON."""
        # TODO Реализуйте код загрузки данных с файла. Помните, что файла может не существовать
        try:
            # Пытаемся открыть файл для чтения
            with open(self.filename, 'r', encoding='utf-8') as file:
                tasks_data = json.load(file)

                # Преобразуем словари обратно в объекты Task
            self.tasks = [Task.from_dict(task_data) for task_data in tasks_data]

            if self.tasks:
                print(f"📂 Загружено {len(self.tasks)} задач из файла '{self.filename}'")
        except FileNotFoundError:
            # Если файла нет - это нормально, просто создаем пустой список
            print(f"📝 Файл '{self.filename}' не найден. Будет создан новый список задач.")
            self.tasks = []
        except json.JSONDecodeError:
            # Если файл поврежден
            print(f"⚠️ Ошибка чтения файла '{self.filename}'. Файл поврежден. Создан пустой список.")
            self.tasks = []
        except Exception as e:
            print(f"❌ Неожиданная ошибка при загрузке: {e}")
            self.tasks = []

    def add_task(self, task: Task) -> None:
        """
        Добавляет задачу в список и сохраняет в файл.

        Args:
            task: Объект задачи для добавления.
        """
        # TODO Реализуйте код
        self.tasks.append(task)
        print(f"✅ Задача '{task.title}' добавлена!")
        self.save_to_file()

    def list_tasks(self) -> None:
        """Выводит все задачи с их порядковыми номерами (начиная с 1).
        Если задач нет, то выводит сообщение 'Список задач пуст!'"""
        # TODO Реализуйте код
        if not self.tasks:
            print("\n📋 Список задач пуст!")
            return

        print("\n" + "="*50)
        print("📋 ВАШИ ЗАДАЧИ:")
        print("="*50)
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")
            if task.description:
                print(f"   📝 Описание: {task.description}")
        print("="*50)

    def mark_task_done(self, index: int) -> None:
        """
        Отмечает задачу как выполненную. Сохраняет изменения в файл.

        Args:
            index: Номер задачи в списке (начиная с 1).

        Raises:
            IndexError: Если номер задачи неверный.
        """
        # TODO Реализуйте код

        if 1 <= index <= len(self.tasks):
            task = self.tasks[index - 1]
            if not task.is_done:
                task.mark_as_done()
                print(f"✅ Задача '{task.title}' отмечена как выполненная!")
            else:
                print(f"ℹ️ Задача '{task.title}' уже была выполнена ранее.")
            self.save_to_file()
        else:
            raise IndexError(f"Неверный номер задачи! Введите число от 1 до {len(self.tasks)}")

    def remove_task(self, index: int) -> None:
        """
        Удаляет задачу из списка. Сохраняет изменения в файл.

        Args:
            index: Номер задачи в списке (начиная с 1).

        Raises:
            IndexError: Если номер задачи неверный.
        """
        # TODO Реализуйте код

        if 1 <= index <= len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            print(f"🗑️ Задача '{removed_task.title}' удалена!")
            self.save_to_file()
        else:
            raise IndexError(f"Неверный номер задачи! Введите число от 1 до {len(self.tasks)}")


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
            print("\n--- Добавление новой задачи ---")
            title = input("Введите название задачи: ")
            description = input("Введите описание (не обязательно): ")
            # TODO Реализуйте логику добавления объекта задачи в объект todo (объект менеджера задач)
            try:
                new_task = Task(title, description)
                todo.add_task(new_task)
            except ValueError as e:
                print(f"❌ Ошибка: {e}")

        elif choice == "3":  # Отметить задачу выполненной
            # TODO Реализуйте функционал
            print("\n--- Отметка задачи как выполненной ---")
            todo.list_tasks()
            if todo.tasks:
                try:
                    index = int(input("Введите номер задачи для отметки: ").strip())
                    todo.mark_task_done(index)
                except ValueError:
                    print("❌ Ошибка: Введите корректное число!")
                except IndexError as e:
                    print(f"❌ {e}")
        elif choice == "4":  # Удалить задачу
            # TODO Реализуйте функционал
            print("\n--- Удаление задачи ---")
            todo.list_tasks()
            if todo.tasks:
                try:
                    index = int(input("Введите номер задачи для удаления: ").strip())
                    todo.remove_task(index)
                except ValueError:
                    print("❌ Ошибка: Введите корректное число!")
                except IndexError as e:
                    print(f"❌ {e}")
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()  # Проверьте работоспособность приложения