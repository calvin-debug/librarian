from rest_framework import serializers
from .models import Book, Author


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'published_date')


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ()


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ()
