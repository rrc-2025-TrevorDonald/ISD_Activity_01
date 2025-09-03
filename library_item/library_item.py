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

    def __init__(self, item_id:int, title:str, author:str, genre:Genre,
                 is_borrowed:bool):
        """
        Description:
            Constructor for LibraryItem class.
        
        Args:
            item_id (int): Id number if the book.
            title (str): Title of the book.
            author (str): Author of the book.
            genre (Genre): Genre of the book.
            is_borrowed (boolean): Is the book taken out.
        
        Raises:
            ValueError(Item id must be numeric.) When the value entered is not
            numeric.
            ValueError(Title cannot be blank.): When no name was entered.
            ValueError(Author cannot be blank.): When no author was entered.
            ValueError(Invalid Genre.): When the genre entered is invalid.
            ValueError(Is Borrowed must be a boolean value.): When the value
            entered in not a boolean.  
        """
        if isinstance(item_id, int):
            self.__item_id = item_id
        else:
            raise ValueError("Item id must be numeric.")

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

        if isinstance(is_borrowed, bool):
            self.__is_borrowed = is_borrowed
        else:
            raise ValueError("Is Borrowed must be a boolean value.")

    @property
    def item_id(self) -> int:
        """
        Description:
            Accessor for private attribute item_id.
        """
        return self.__item_id

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

    @property
    def is_borrowed(self):
        """
        Description:
            Accessor for private attribute is_borrowed.
        """
        return self.__is_borrowed
