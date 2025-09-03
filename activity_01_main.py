""""
Description: A client program written to verify correctness of 
the activity classes.
"""
__author__ = "Trevor Donald"
__version__ = "1.0.0"
__credits__ = "ACE Faculty"

from genre.genre import Genre
from library_item.library_item import LibraryItem

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """
    # In the statements coded below, ensure that any statement that could
    # result in an exception is handled.  When exceptions are 'caught', display
    # the exception message to the console.

    # 1. Code a statement which creates an instance of the LibraryItem class
    # with valid inputs.
    # Use your own unique valid values for the inputs to the class.

    book = LibraryItem("Bible", "Some guy", Genre.FICTION)

    # 2. Using the instance defined above, and the class Accessors, print
    # each of the attributes of the LibraryItem instance.

    print(book.title)
    print(book.author)
    print(book.genre)

    # 3. Code a statement which creates an instance of the LibraryItem class
    # with one or more invalid inputs.
    # Use your own unique valid values for the inputs to the class.
    try:
        book2 = LibraryItem("", "", Genre.TRUE_CRIME)
        print(book2.title)
        print(book2.author)
        print(book2.genre)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
