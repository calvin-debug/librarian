from django.test import TestCase
from library.models import Author, Book
from library.serializers import AuthorSerializer


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

    def test_author_seiralizer(self):
        serializer = AuthorSerializer(self.author)
        data = serializer.data
        self.assertEqual(data['first_name'], 'John')
        self.assertEqual(data['last_name'], 'Doe')
        # self.assertEqual(data['full_name'], 'John Doe')
