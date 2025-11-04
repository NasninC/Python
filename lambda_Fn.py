# Lambda functions for area calculations
square_area = lambda side: side * side
rectangle_area = lambda length, breadth: length * breadth
triangle_area = lambda base, height: 0.5 * base * height

# --- Main program ---
side = float(input("Enter side of square: "))
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))

print("Area of Square:", square_area(side))
print("Area of Rectangle:", rectangle_area(length, breadth))
print("Area of Triangle:", triangle_area(base, height))
