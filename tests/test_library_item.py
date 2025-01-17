"""
Description: Unit tests for the Book class.
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_book.py

"""
__author__ = ""
__version__ = ""

import unittest
from genre.genre import Genre
from library_item.library_item import LibraryItem


class TestLibraryItem(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.item = LibraryItem("DUNE", "Frank Herbert", Genre.FICTION)

    def test_init_valid_inputs_attributes_set(self):
        # Arrange & Act
        item = LibraryItem("Dune", "Frank Herbert", Genre.FICTION)

        # Assert
        self.assertEqual("Dune", item._LibraryItem__title)
        self.assertEqual("Frank Herbert", item._LibraryItem__author)
        self.assertEqual(Genre.FICTION, item._LibraryItem__genre)

    def test_init_blank_title_raises_valueerror(self):
        with self.assertRaises(ValueError):
            LibraryItem("", "Frank Herbert", Genre.FICTION)

    def test_init_blank_author_raises_valueerror(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            LibraryItem("Dune", "", Genre.FICTION)

    def test_init_invalid_genre_raises_valueerror(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            LibraryItem("DUNE", "Frank Herbert", "INVALID")

    def test_title_accessor_valid_title_returns_attribute(self):
        # Act & Assert
        self.assertEqual("DUNE", self.item.title)

    def test_author_accessor_valid_author_returns_attribute(self):
        # Act & Assert
        self.assertEqual("Frank Herbert", self.item.author)

    def test_genre_accessor_valid_genre_returns_attribute(self):
        # Act & Assert
        self.assertEqual(Genre.FICTION, self.item.genre)
