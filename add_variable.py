def add_numbers(*nums):
    """Return the sum of all given numbers."""
    return sum(nums)

# Main program
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sum =", add_numbers(*numbers))
