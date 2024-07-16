from django.test import TestCase, RequestFactory
from library.models import Author, Book
from rest_framework import status
from library.views import BookViewSet


class Block4Tests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.author = Author.objects.create(first_name='John', last_name='Doe', age=45)

        for i in range(50):
            Book.objects.create(
                title=f'Book {i}',
                author=self.author,
                authored_date='2022-01-01',
                published_date='2023-01-01' if i % 2 == 0 else None,
                pages=200 + i,
            )

    def test_books_pagination(self):
        request = self.factory.get('/books/')
        view = BookViewSet.as_view({'get': 'list'})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('count', response.data)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)
        self.assertIn('results', response.data)
        self.assertEqual(len(response.data['results']), 10)