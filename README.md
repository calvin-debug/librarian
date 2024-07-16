

## Block 1 - Serializers

### Files to work on
- `library/models.py`
- `library/serializers.py`
- `library/views.py`

### Tasks
1. Implement missing serializers for `BookDetailSerializer` and `AuthorSerializer`. 
   1. The `BookDetailSerializer` should include the page count author details and also all the fields from the `BookListSerializer`.
   2. `AuthorSerializer` should include all fields from the `Author` model.
   3. The `AuthorSerializer` should include a custom field for `book_count` that represents the number of books written by that author.

### Running tests
- Run the tests using the command `python manage.py test library.tests.test_block_1`.

## Block 2 -- Views

### Files to work on
- `library/models.py`
- `library/serializers.py`
- `library/views.py`

### Tasks
1. There is a large inefficiency in the `BookViewSet` when it comes to retrieving a specific book. Find it and optimise the implemented solution.
2. Currently, the newly created `BookDetailSerializer` is not being used in the `BookViewSet`. Modify the `BookViewSet` to use the `BookDetailSerializer` when retrieving a single book.
3. Create another viewset for the `Author` model. This viewset should have the following features:
   1. It should be possible to create new authors. The view should use the `AuthorSerializer` for both creating and retrieving authors
      1. If needed, implement the `create` method in the `AuthorSerializer` to handle the creation of new authors.
   2. It should be possible to both list all authors and retrieve a single author.
   3. There should be an action in the view that retrieves all the books written by that author. The books should be serialized using the `BookListSerializer`

### Running tests
- Run the tests using the command `python manage.py test library.tests.test_block_2`.


## Block 3 -- Models

### Files to work on
- `library/models.py`

### Tasks
1. Look at the model for `Author`. Create a new property in the model that would represent the full name of the author, using the `@property` decorator.
2. Create a new model called `Publisher`. This model should have the following fields:
   1. `name` - a non-nullable CharField with a maximum length of 100 characters.
   2. `country` - a CharField with a maximum length of 100 characters.
3. Create a connection between the `Book` and `Publisher` models. A book could have one publisher, but a publisher can have multiple books. A book can be without a publisher.
4. Create and run the migrations to reflect the new database schema.


## Block 4 -- Filtering

### Files to work on
- `library/views.py`
- `library/filters.py`

### Tasks
1. The initial queryset used by the `BookViewSet` includes all books. Modify this to only include books that have already been published. This means only books that have a value for `published_date` set should be included.
2. Create a new filter for the `BookViewSet` that allows to filter books based on the title. The filtering should use the query parameter `search` for filtering This search should be case-insensitive. You can implement the filter as a filter backend or do the filtering in the viewset itself. If stuck, see documentation here: [DRF custom filters](https://www.django-rest-framework.org/api-guide/filtering/#custom-generic-filtering)

### Running tests
- Run the tests using the command `python manage.py test library.tests.test_block_4`.


## Block 5 -- Pagination

### Files to work on
- `library/views.py`
- `library/pagination.py`

### Tasks
1. Implement pagination for the `BookViewSet`. The pagination should be done using the `PageNumberPagination` class and should include 10 books per page. The pagination backend has been initialized, but not set up correctly in the `library/pagination.py` file. If stuck, see documentation here: [DRF custom pagination](https://www.django-rest-framework.org/api-guide/pagination/)

### Running tests
- Run the tests using the command `python manage.py test library.tests.test_block_5`.

