# Librarian | Django REST Framework mock project

## Setup guide
1. Clone the repository
2. Create a virtual environment using `python -m venv venv` (or `python3 -m venv venv` on Linux-based systems)
3. Activate the virtual environment using `source venv/bin/activate` on Linux-based systems or `venv\Scripts\activate` on Windows
4. Install the dependencies using `pip install -r requirements.txt`
5. Run the migrations using `python manage.py migrate`
6. Start solving the tasks

## Goals
1. The goal of each block is to implement the missing functionality in the Django REST Framework project.
2. Each block has a set of tasks that need to be completed and a set of tests that need to be passed.
3. Once you have completed the tasks, run the tests to verify that the implementation is correct.
4. You can also run any individual test case to verify the implementation. For example, `python manage.py test library.tests.test_block_1.Block1Tests.test_author_serializer`.
5. If you have any questions, feel free to ask the interviewer.


# Tasks

## Block 1 - Serializers

### Files to work on
- `library/serializers.py`

### Tasks
1. Implement missing serializers for `BookDetailSerializer` and `AuthorSerializer`. 
   1. `AuthorSerializer` should include all fields from the `Author` model.
   2. The `AuthorSerializer` should include a custom field for `book_count` that represents the number of books written by that author.
   3. The `BookDetailSerializer` should include the page count author details and also all the fields from the `BookListSerializer`.

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

### Running tests
- Run the tests using the command `python manage.py test library.tests.test_block_3`.


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

