from rest_framework import viewsets
from .models import Book, Author
from . import serializers


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    # filter_backends = []
    serializer_class = serializers.BookListSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        for book in Book.objects.all():
            if book.pk == pk:
                return book


# class AuthorViewSet(viewsets.ModelViewSet):
#     queryset = Author.objects.all()


# class AuthorViewSet(viewsets.ModelViewSet):
#     queryset = Author.objects.all()
