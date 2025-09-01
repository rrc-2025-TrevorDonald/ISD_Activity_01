""""
Description: A class to manage LibraryItem objects.
"""
__author__ = "Trevor Donald"
__version__ = "1.0.0"

from genre.genre import Genre

class LibraryItem():
    """
    """

    def __init__(self, title:str, author:str, genre:Genre):
        """
        """
        if len(title) > 0:
            self.__title = title
        else:
            raise ValueError("Title cannot be blank.")

        if len(author) > 0:
            self.__author = author
        else:
            raise ValueError("Author cannot be blank.")

        if isinstance(genre, Genre):
            self.__genre = genre
        else:
            raise ValueError("Invalid Genre.")
