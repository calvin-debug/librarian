from django.test import TestCase, RequestFactory
from library.models import Author, Book, Publisher


class Block3Tests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.author = Author.objects.create(first_name='John', last_name='Doe', age=45)

    def test_author_full_name_property(self):
        self.assertGreaterEqual(len(self.author.full_name), len(self.author.first_name) + len(self.author.last_name))

    def test_book_publisher_set(self):
        publisher = Publisher.objects.create(name='Test Publisher', country='Estonia')
        book = Book.objects.create(
            title='Test Book',
            authored_date='2022-01-01',
            published_date='2023-01-01',
            pages=200,
            publisher=publisher,
            author=self.author
        )

        self.assertEqual(book.publisher, publisher)

    def test_book_publisher_not_set(self):
        book = Book.objects.create(
            title='Test Book',
            authored_date='2022-01-01',
            published_date='2023-01-01',
            pages=200,
            author=self.author
        )

        self.assertIsNone(book.publisher)
        self.assertEqual(Book.objects.count(), 1)

