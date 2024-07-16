from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()


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
