""""
Description: A client program written to verify correctness of 
the activity classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Philip Pacla-on"

from genre.genre import Genre
from library_item.library_item import LibraryItem


def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """
    # In the statements coded below, ensure that any statement that could result
    # in an exception is handled.  When exceptions are 'caught', display the exception
    # message to the console.

    # 1. Code a statement which creates an instance of the LibraryItem class with valid inputs.
    # Use your own unique valid values for the inputs to the class.

    valid_item = LibraryItem(
        1, "Harry Potter", "J.K Rowling", Genre.FANTASY, False)

    # 2. Using the instance defined above, and the class Accessors, print
    # each of the attributes of the LibraryItem instance.
    try:
        print(f"Item ID: {valid_item.item_id}")
        print(f"Title: {valid_item.title}")
        print(f"Author: {valid_item.author}")
        print(f"Genre: {valid_item.genre}")
        print(f"Is Borrowed: {valid_item.is_borrowed}")
    except ValueError as e:
        print(f"Error: {e}")
    # 3. Code a statement which creates an instance of the LibraryItem class with one or more invalid inputs.
    # Use your own unique valid values for the inputs to the class.
    try:
        invalid_item = LibraryItem(1, "", "J.K Rowling", Genre.FANTASY, False)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        invalid_item = LibraryItem(
            1, "Harry Potter", "J.K Rowling", "INVALID", False)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
