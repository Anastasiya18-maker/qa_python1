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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('1984')  # Пробуем добавить дубликат

        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Убить пересмешника')
        collector.set_book_genre('Убить пересмешника', 'Фантастика')

        assert collector.get_book_genre('Убить пересмешника') == 'Фантастика'

    def test_set_book_genre_invalid(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Неизвестный жанр')  # Жанр не существует

        assert collector.get_book_genre('Властелин колец') == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Мост через реку Квай')
        collector.set_book_genre('Мост через реку Квай', 'Фантастика')

        collector.add_new_book('Невыносимая легкость бытия')
        collector.set_book_genre('Невыносимая легкость бытия', 'Фантастика')

        books = collector.get_books_with_specific_genre('Фантастика')
        assert len(books) == 2

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
        collector.set_book_genre('Светлячок', 'Комедии')

        collector.add_book_in_favorites('Светлячок')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Детективы')

        collector.add_book_in_favorites('Преступление и наказание')
        collector.delete_book_from_favorites('Преступление и наказание')
        assert len(collector.get_list_of_favorites_books()) == 0

    @pytest.mark.parametrize("book_name, expected_length", [
        ('Краткая история времени', 1),
        ('Сумерки', 2),
    ])
    def test_add_and_search_multiple_books(self, book_name, expected_length):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Фантастика')

        collector.add_new_book('Новая книга')
        collector.set_book_genre('Новая книга', 'Комедии')

        assert len(collector.get_books_genre()) == expected_length
