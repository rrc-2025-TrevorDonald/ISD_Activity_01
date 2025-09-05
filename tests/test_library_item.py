"""
Description: Unit tests for the Book class.
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_book.py

"""
__author__ = "Trevor Donald"
__version__ = "1.0.0"

import unittest
from library_item.library_item import LibraryItem
from genre.genre import Genre

class TestClient(unittest.TestCase):
    """
    Description:
        Class defined for testing all functions of the LibraryItem class.
    """

    def setUp(self):
        """
        Description:
            Setup function for simplifying tests
        """
        self.libraryitem = LibraryItem(9,"The_Lord_of_the_Rings",
                                       "J.R.R. Tolkien", Genre.FANTASY, True)

    def test_init_valid(self):
        """
        Description:
            Test function for testing the constructor of LibraryItem.
        """
        library_item = LibraryItem(
                9, "The_Lord_of_the_Rings", "J.R.R. Tolkien", Genre.FANTASY,
                True)

        self.assertEqual(9, library_item._LibraryItem__item_id)
        self.assertEqual("The_Lord_of_the_Rings",
                         library_item._LibraryItem__title)
        self.assertEqual("J.R.R. Tolkien", library_item._LibraryItem__author)
        self.assertEqual(Genre.FANTASY, library_item._LibraryItem__genre)
        self.assertEqual(True, library_item._LibraryItem__is_borrowed)

    def test_init_item_id_valid(self):
        """
        Description:
            Test function for testing to ensure the proper value error is
            being thrown for item_id.
        """
        with self.assertRaises(ValueError):
            LibraryItem("9", "The_Lord_of_the_Rings",
                        "J.R.R. Tolkien", "Invalid", True)

    def test_init_title_valid(self):
        """
        Description:
            Test function for testing to ensure the proper value error is
            being thrown for title.
        """
        expected = "Title cannot be blank."
        with self.assertRaises(ValueError) as exception:
            LibraryItem(9, "", "J.R.R. Tolkien", Genre.FANTASY, True)

        self.assertEqual(expected, str(exception.exception))

    def test_init_author_valid(self):
        """
        Description:
            Test function for testing to ensure the proper value error is
            being thrown for author.
        """
        with self.assertRaises(ValueError):
            LibraryItem(9, "The_Lord_of_the_Rings", "", Genre.FANTASY, True)

    def test_init_genre_valid(self):
        """
        Description:
            Test function for testing to ensure the proper value error is
            being thrown for genre.
        """
        with self.assertRaises(ValueError):
            LibraryItem(9, "The_Lord_of_the_Rings",
                        "J.R.R. Tolkien", "Invalid", True)

    def test_init_is_borrowed_valid(self):
        """
        Description:
            Test function for testing to ensure the proper value error is
            being thrown for is_borrowed.
        """
        with self.assertRaises(ValueError):
            LibraryItem(9, "The_Lord_of_the_Rings",
                        "J.R.R. Tolkien", Genre.FANTASY, "Invalid")

    def test_item_id_accessor(self):
        """
        Description:
            Test function for testing the accessor for item_id.
        """
        self.assertEqual(9, self.libraryitem.item_id)

    def test_title_accessor(self):
        """
        Description:
            Test function for testing the accessor for title.
        """
        self.assertEqual("The_Lord_of_the_Rings", self.libraryitem.title)

    def test_author_accessor(self):
        """
        Description:
            Test function for testing the accessor for author.
        """
        self.assertEqual("J.R.R. Tolkien", self.libraryitem.author)

    def test_genre_accessor(self):
        """
        Description:
            Test function for testing the accessor for genre.
        """
        self.assertEqual(Genre.FANTASY, self.libraryitem.genre)

    def test_is_borrowed_accessor(self):
        """
        Description:
            Test function for testing the accessor for is_borrowed.
        """
        self.assertEqual(True, self.libraryitem.is_borrowed)
