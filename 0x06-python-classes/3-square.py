#!/usr/bin/python3

"""Define a class Square."""

class Square:
    """Define a class Square."""

    def __init__(self,size=0):
        """Define a class Square."""
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif( size < 0):
            raise ValueError("size must be >= 0")
        self.__size=size
    def area(self):
        """Define a class Square."""
        return (self.__size**2)
