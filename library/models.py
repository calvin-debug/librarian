from django.db import models


# TODO find the number of books in the library
# TODO find the book with the longest title
# class Library(models.Model):


# TODO find the first book that the author has published
# TODO create a property that returns the full name of the author. Include this in the serializer
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()


# TODO find all books that were published after 2010
# TODO find all books with a page count greater than 100
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    authored_date = models.DateField()
    published_date = models.DateField(
        null=True,
        help_text="""
            The date the book was published. If not set, the book has not yet
            been published.
        """
    )
    pages = models.IntegerField()
