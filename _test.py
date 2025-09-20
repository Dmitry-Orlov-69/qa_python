import pytest
from main import BooksCollector

class TestBooksCollector:
    @pytest.mark.parametrize("title, expected_result", [
        ("Война и мир", True),
        ("a" * 41, False)
    ])
    def test_add_new_book(self, title, expected_result):
        collector = BooksCollector()
        collector.add_new_book(title)
        assert (title in collector.books_genre) == expected_result

    @pytest.mark.parametrize("book_title, genre", [
        ("Преступление и наказание", "Детективы"),
        ("Великий Гэтсби", "Фантастика")
    ])
    def test_set_book_genre(self, book_title, genre):
        collector = BooksCollector()
        collector.add_new_book(book_title)
        collector.set_book_genre(book_title, genre)
        genre_from_collector = collector.get_book_genre(book_title)
        assert genre_from_collector == genre

    @pytest.mark.parametrize("book_title, genre", [
        ("Преступление и наказание", "Детективы"),
        ("Великий Гэтсби", "Фантастика")
    ])
    def test_get_book_genre(self, book_title, genre):
        collector = BooksCollector()
        collector.add_new_book(book_title)
        # Устанавливаем жанр напрямую в словарь, без использования метода set_book_genre
        collector.books_genre[book_title] = genre
        genre_from_collector = collector.get_book_genre(book_title)
        assert genre_from_collector == genre

    @pytest.mark.parametrize("book_title, genre", [
        ("Гарри Поттер", "Фантастика"),
        ("Мастер и Маргарита", "Фантастика")
    ])
    def test_get_books_with_specific_genre(self, book_title, genre):
        collector = BooksCollector()
        collector.add_new_book(book_title)
        collector.set_book_genre(book_title, genre)
        books = collector.get_books_with_specific_genre(genre)
        assert book_title in books

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Фантастика')
        books_genre = collector.get_books_genre()
        assert books_genre == {'Мастер и Маргарита': 'Фантастика'}

    @pytest.mark.parametrize("book_title, genre", [
        ("Кот в сапогах", "Мультфильмы"),
        ("Приключения Тома Сойера", "Мультфильмы")
    ])
    def test_get_books_for_children(self, book_title, genre):
        collector = BooksCollector()
        collector.add_new_book(book_title)
        collector.set_book_genre(book_title, genre)
        children_books = collector.get_books_for_children()
        assert book_title in children_books

    @pytest.mark.parametrize("book_title", [
        ("Ромео и Джульетта"),
        ("1984")
    ])
    def test_add_book_in_favorites(self, book_title):
        collector = BooksCollector()
        collector.add_new_book(book_title)
        collector.add_book_in_favorites(book_title)
        assert book_title in collector.favorites

    @pytest.mark.parametrize("book_title", [
        ("Ромео и Джульетта"),
        ("1984")
    ])
    def test_delete_book_from_favorites(self, book_title):
        collector = BooksCollector()
        collector.add_new_book(book_title)
        collector.add_book_in_favorites(book_title)
        collector.delete_book_from_favorites(book_title)
        assert book_title not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Унесенные ветром')
        collector.add_book_in_favorites('Унесенные ветром')
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['Унесенные ветром']