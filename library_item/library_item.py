""""
Description: A class to manage LibraryItem objects.
"""
__author__ = "Philip Pacla-on"
__version__ = "1.0.0"

from genre.genre import Genre


class LibraryItem:
    """
    LibraryItem Class: Manages LibraryItem objects.

    """

    def __init__(self, title: str, author: str, genre: Genre):
        """

        """
        if len(title.strip()) > 0:
            self.__title = title
        else:
            raise ValueError("Title cannot be blank.")

        if len(author.strip()) > 0:
            self.__author = author
        else:
            raise ValueError("Author cannot be blank.")

        if isinstance(genre, Genre):
            self.__genre = genre
        else:
            raise ValueError("Invalid Genre.")

    @property
    def title(self) -> str:
        """
        """
        return self.__title

    @property
    def author(self) -> str:
        """
        """
        return self.__author

    @property
    def genre(self) -> Genre:
        """
        """
        return self.genre
