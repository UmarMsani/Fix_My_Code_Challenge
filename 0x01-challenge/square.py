#!/usr/bin/python3
"""
Square class
"""


class Square():
    """
    starting the class representing a square shape.

    Attributes:
    - width: The width of the square.
    - height: The height of the square.
    """

    def __init__(self, width, height):
        """
        Initialize the Square object with provided width and height

        Args:
        - width: width of the square.
        - height: Height of the square.
        """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """
        Calculate the area of the square.

        Returns:
        The perimeter of the square
        """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """
        calculate the perimeter of the square.

        Returns:
        the perimeter of the square
        """
        return 4 * self.width

    def __str__(self):
        """
        Represent the square's dimensions as a string.

        Returns:
        string representation of square in the format 'width/height'.
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
