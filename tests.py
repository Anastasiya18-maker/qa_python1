import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('1984')  # Пробуем добавить дубликат

        assert len(collector.books_genre) == 1

    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Убить пересмешника')
        assert collector.books_genre['Убить пересмешника'] == ''
        collector.set_book_genre('Убить пересмешника', 'Фантастика')

        assert collector.books_genre['Убить пересмешника'] == 'Фантастика'

    def test_set_book_genre_invalid(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        assert collector.books_genre['Властелин колец'] == ''
        collector.set_book_genre('Властелин колец', 'Неизвестный жанр')  # Жанр не существует

        assert collector.books_genre['Властелин колец'] == '' # Проверка метода get_book_genre!

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        assert collector.get_book_genre('Властелин колец') == ''
        collector.set_book_genre('Властелин колец', 'Ужасы')  # Жанр не существует

        assert collector.get_book_genre('Властелин колец') == 'Ужасы'

    def test_get_book_genre_invalid(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Властелин колец') is None


    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Мост через реку Квай')
        collector.set_book_genre('Мост через реку Квай', 'Фантастика')

        collector.add_new_book('Невыносимая легкость бытия')
        collector.set_book_genre('Невыносимая легкость бытия', 'Фантастика')

        books = collector.get_books_with_specific_genre('Фантастика')
        assert len(books) == 2

    def test_get_books_genre(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}
        collector.add_new_book('Мост через реку Квай')
        collector.set_book_genre('Мост через реку Квай', 'Фантастика')
        assert collector.get_books_genre() == {'Мост через реку Квай': 'Фантастика'}

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Паддингтона')
        collector.set_book_genre('Приключения Паддингтона', 'Мультфильмы')

        collector.add_new_book('Кубо. Легенда о самурае')
        collector.set_book_genre('Кубо. Легенда о самурае', 'Ужасы')  # Для детей не подходит

        children_books = collector.get_books_for_children()
        assert len(children_books) == 1

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Светлячок')


        collector.add_book_in_favorites('Светлячок')
        assert collector.favorites == ['Светлячок']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Детективы')

        collector.add_book_in_favorites('Преступление и наказание')
        collector.delete_book_from_favorites('Преступление и наказание')
        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []
        collector.add_new_book('Преступление и наказание')
        collector.add_book_in_favorites('Преступление и наказание')
        assert collector.get_list_of_favorites_books() == ['Преступление и наказание']

    @pytest.mark.parametrize("book_name, additional_book, expected_length", [
        ('Краткая история времени', 'Новая книга', 2),
        ('Сумерки', 'Пандемониум', 2),
    ])
    def test_add_and_search_multiple_books(self, book_name, additional_book, expected_length):
        collector = BooksCollector()

        # Добавление первой книги
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Фантастика')

        # Добавление дополнительной книги
        collector.add_new_book(additional_book)
        collector.set_book_genre(additional_book, 'Комедия')

        # Проверка количества книг
        assert len(collector.get_books_genre()) == expected_length


