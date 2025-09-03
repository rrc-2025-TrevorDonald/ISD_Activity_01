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

    def setUp(self):
        self.libraryitem = LibraryItem("The_Lord_of_the_Rings",
                                       "J.R.R. Tolkien", Genre.FANTASY)

    def test_init_valid(self):
        library_item = LibraryItem(
            "The_Lord_of_the_Rings", "J.R.R. Tolkien", Genre.FANTASY)

        self.assertEqual("The_Lord_of_the_Rings",
                         library_item._LibraryItem__title)
        self.assertEqual("J.R.R. Tolkien", library_item._LibraryItem__author)
        self.assertEqual(Genre.FANTASY, library_item._LibraryItem__genre)

    def test_init_title_valid(self):
        expected = "Title cannot be blank."
        with self.assertRaises(ValueError) as exception:
            LibraryItem("", "J.R.R. Tolkien", Genre.FANTASY)

        self.assertEqual(expected, str(exception.exception))

    def test_init_author_valid(self):
        with self.assertRaises(ValueError):
            LibraryItem("The_Lord_of_the_Rings", "", Genre.FANTASY)

    def test_init_genre_valid(self):
        with self.assertRaises(ValueError):
            LibraryItem("The_Lord_of_the_Rings", "J.R.R. Tolkien", "Invalid")

    def test_title_accessor(self):
        self.assertEqual("The_Lord_of_the_Rings", self.libraryitem.title)

    def test_author_accessor(self):
        self.assertEqual("J.R.R. Tolkien", self.libraryitem.author)

    def test_genre_accessor(self):
        self.assertEqual(Genre.FANTASY, self.libraryitem.genre)
