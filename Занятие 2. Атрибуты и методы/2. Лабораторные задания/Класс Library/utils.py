"""Ручная загрузка модуля ввиду сложного пути загрузки"""
import importlib.util
import sys
from pathlib import Path

base = Path(Path.cwd())

# Указываем путь к файлу модуля
file_path = base.parent / 'Класс Book' / 'main.py'
module_name = "main"

# Создаём спецификацию модуля
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module  # Добавляет модуль в системный кеш загруженных модулей
spec.loader.exec_module(module) # Выполняет код модуля в его собственном пространстве имён

Book = module.Book