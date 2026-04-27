import unittest

from task import Book, PaperBook, AudioBook


class TestBook(unittest.TestCase):
    def test1_protected_attrs(self):
        book = Book('A', 'A')
        self.assertTrue(hasattr(book, '_name'), 'Book не содержит атрибут _name')
        self.assertTrue(hasattr(book, '_author'), 'Book не содержит атрибут _author')

    def test2_property(self):
        book = Book('A', 'A')
        with self.assertRaises(AttributeError, msg='Не реализовано свойство только на чтение для name'):
            book.name = 'B'

        with (self.assertRaises(AttributeError, msg='Не реализовано свойство только на чтение для author')):
            book.author = 'B'

class TestPaperBook(unittest.TestCase):
    def test1_inheritance(self):
        self.assertTrue(issubclass(PaperBook, Book), 'Не реализовано наследование от Book')

    def test2_pages(self):
        with self.assertRaises(TypeError, msg='Нет проверки типа для pages'):
            PaperBook('A', 'A', 'A')
        with self.assertRaises(ValueError, msg='Нет проверки ограничения значений для pages'):
            PaperBook('A', 'A', 0)

    def test3_repr(self):
        text = repr(PaperBook('A', 'A', 100))
        self.assertEqual(text, "PaperBook(name='A', author='A', pages=100)")

class TestAudioBook(unittest.TestCase):
    def test1_inheritance(self):
        self.assertTrue(issubclass(AudioBook, Book), 'Не реализовано наследование от Book')

    def test2_duration(self):
        with self.assertRaises(TypeError, msg='Нет проверки типа для duration'):
            AudioBook('A', 'A', 'A')
        with self.assertRaises(ValueError, msg='Нет проверки ограничения значений для duration'):
            AudioBook('A', 'A', 0.0)

    def test3_repr(self):
        text = repr(AudioBook('A', 'A', 100.0))
        self.assertEqual(text, "AudioBook(name='A', author='A', duration=100.0)")