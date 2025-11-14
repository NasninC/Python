# Base class
class Publisher:
    def __init__(self, name):
        self.name = name

    # Method to display publisher info (can be overloaded in subclasses)
    def display(self):
        print(f"Publisher: {self.name}")


# Derived class from Publisher
class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)                 # Base class constructor invocation
        self.title = title
        self.author = author

    # Overloaded display method
    def display(self):
        super().display()                      # Call base class display
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


# Derived class from Book
class Python(Book):
    def __init__(self, name, title, author, price, pages):
        super().__init__(name, title, author)  # Base class constructor invocation
        self.price = price
        self.pages = pages

    # Further overloaded display method
    def display(self):
        super().display()
        print(f"Price: ₹{self.price}")
        print(f"Pages: {self.pages}")


# ---------------------------
# Driver Code
# ---------------------------

# Create a Python book object
py_book = Python(
    name="O'Reilly Media",
    title="Learning Python",
    author="Mark Lutz",
    price=750,
    pages=1648
)

# Display full information
py_book.display()
