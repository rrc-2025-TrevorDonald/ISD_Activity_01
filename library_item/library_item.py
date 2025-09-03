""""
Description: A class to manage LibraryItem objects.
"""
__author__ = "Trevor Donald"
__version__ = "1.0.0"

from genre.genre import Genre

class LibraryItem():
    """
    Description:
        Class defined for performing functions of a Library Item.
    """

    def __init__(self, title:str, author:str, genre:Genre):
        """
        Description:
            Constructor for LibraryItem class.
        
        Args:
            title (str): Title of the book.
            author (str): Author of the book.
            genre (Genre): Genre of the book.
        
        Raises:
            ValueError(Title cannot be blank): When no name was entered
            ValueError(Author cannot be blank): When no author was entered
            ValueError(Invalid Genre): When the genre entered is invalid
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

    @property
    def title (self) -> str:
        """
        Description:
            Accessor for private attribute title.
        """
        return self.__title

    @property
    def author(self) -> str:
        """
        Description:
            Accessor for private attribute author.
        """
        return self.__author

    @property
    def genre(self) -> Genre:
        """
        Description:
            Accessor for private attribute genre.
        """
        return self.__genre
