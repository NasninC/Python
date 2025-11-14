class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        """Return the area of the rectangle."""
        return self.length * self.breadth

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.length + self.breadth)

    def __lt__(self, other):
        """Compare rectangles by area (less than)."""
        return self.area() < other.area()

    def __eq__(self, other):
        """Check if two rectangles have equal area."""
        return self.area() == other.area()

# Example usage
rect1 = Rectangle(10, 5)
rect2 = Rectangle(8, 6)

print("Area of Rectangle 1:", rect1.area())
print("Perimeter of Rectangle 1:", rect1.perimeter())

print("Area of Rectangle 2:", rect2.area())
print("Perimeter of Rectangle 2:", rect2.perimeter())

# Comparing rectangles
if rect1 == rect2:
    print("Both rectangles have the same area.")
elif rect1 < rect2:
    print("Rectangle 1 has a smaller area than Rectangle 2.")
else:
    print("Rectangle 1 has a larger area than Rectangle 2.")
