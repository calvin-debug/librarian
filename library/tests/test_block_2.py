from django.test import TestCase, RequestFactory
from library.models import Author, Book
from rest_framework import status
from library.views import BookViewSet, AuthorViewSet


class Block2Tests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.author_1 = Author.objects.create(first_name='John', last_name='Doe', age=45)
        self.author_2 = Author.objects.create(first_name='Mary', last_name='Ann', age=18)
        self.book = Book.objects.create(
            title='Author 1 book 1',
            author=self.author_1,
            authored_date='2022-01-01',
            published_date='2023-01-01',
            pages=200
        )
        self.unpublished_book = Book.objects.create(
            title='Author 1 book 2',
            author=self.author_1,
            authored_date='2022-01-01',
            pages=200
        )
        Book.objects.create(
            title='Author 2 book 1',
            author=self.author_2,
            authored_date='2022-01-01',
            published_date='2019-01-01',
            pages=200
        )

    def test_book_object_retrieval(self):
        request = self.factory.get('/books/')
        view = BookViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=self.book.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_book_object_retrieval_no_match(self):
        request = self.factory.get('/books/')
        view = BookViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=100)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_conditional_serializer_usage(self):
        request = self.factory.get('/books/')
        view = BookViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=self.book.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["pages"], self.book.pages)

        view = BookViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotIn("pages", response.data)

    def test_author_create(self):
        new_author = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'age': 35
        }

        authors_before = Author.objects.count()

        request = self.factory.post('/authors/', new_author)
        view = AuthorViewSet.as_view({'post': 'create'})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), authors_before + 1)

        self.assertEqual(response.data["first_name"], new_author["first_name"])

    def test_author_create_incomplete_data(self):
        new_author = {
            'first_name': 'Jane',
            'age': 35
        }

        authors_before = Author.objects.count()

        request = self.factory.post('/authors/', new_author)
        view = AuthorViewSet.as_view({'post': 'create'})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Author.objects.count(), authors_before)

    def test_authors_list(self):
        request = self.factory.get('/authors/')
        view = AuthorViewSet.as_view({'get': 'list'})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Author.objects.count())

    def test_author_retrieve(self):
        request = self.factory.get('/authors/')
        view = AuthorViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=self.author_1.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.author_1.first_name)

    def test_author_retrieve_no_match(self):
        request = self.factory.get('/authors/')
        view = AuthorViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=100)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_author_books_get(self):
        request = self.factory.get('/authors/')
        view = AuthorViewSet.as_view({'get': 'books'})
        response = view(request, pk=self.author_1.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.author_1.book_set.count())

    def test_author_books_get_no_match(self):
        request = self.factory.get('/authors/')
        view = AuthorViewSet.as_view({'get': 'books'})
        response = view(request, pk=100)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)