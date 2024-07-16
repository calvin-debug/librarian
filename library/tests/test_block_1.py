from django.test import TestCase
from library.models import Author, Book
from library.serializers import AuthorSerializer, BookDetailSerializer


class Block1Tests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name='John', last_name='Doe', age=45)
        self.book = Book.objects.create(
            title='Test Book',
            author=self.author,
            authored_date='2022-01-01',
            published_date='2023-01-01',
            pages=200
        )

    def test_author_serializer(self):
        serializer = AuthorSerializer(self.author)
        data = serializer.data
        self.assertEqual(data['first_name'], self.author.first_name)
        self.assertEqual(data['last_name'], self.author.last_name)
        self.assertEqual(data['book_count'], 1)
        self.assertEqual(data['age'], self.author.age)

    def test_book_detail_serializer(self):
        serializer = BookDetailSerializer(self.book)
        data = serializer.data
        self.assertEqual(data['title'], 'Test Book')
        self.assertEqual(data['published_date'], '2023-01-01')
        self.assertEqual(data['pages'], 200)
        self.assertEqual(data['author']['first_name'], self.author.first_name)
