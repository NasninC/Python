class Rectangle:
    def __init__(self, length, width):
        """Initialize private attributes for the rectangle."""
        self.__length = length     # Private attribute
        self.__width = width       # Private attribute

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__length * self.__width

    def __lt__(self, other):
        """Overload < operator to compare rectangles by area."""
        return self.area() < other.area()

    def display(self):
        """Display rectangle details."""
        print(f"Length: {self.__length}, Width: {self.__width}, Area: {self.area()}")


# Example usage
rect1 = Rectangle(10, 5)
rect2 = Rectangle(8, 7)

rect1.display()
rect2.display()

# Compare rectangles using overloaded < operator
if rect1 < rect2:
    print("Rectangle 1 has a smaller area than Rectangle 2.")
else:
    print("Rectangle 1 has a larger or equal area than Rectangle 2.")
