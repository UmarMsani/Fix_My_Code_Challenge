#!/usr/bin/python3


class Square:
    def __init__(self, width, height):
        # Initialize the Square object with provided width and height
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Calculate the area of the square """
        return self.width * self.height  # Area = width * height

    def perimeter_of_my_square(self):
        """ Calculate the perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Represent the square's dimensions as a string """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    # Create a Square object with width=12 and height=9
    s = Square(width=12, height=9)

    # Display the square's dimensions, area, and perimeter
    print(s)  # Print the dimensions of the square
    print(s.area_of_my_square())  # Print the area of the square
    print(s.perimeter_of_my_square())
