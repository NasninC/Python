# Function to find factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# --- Main program ---
n = int(input("Enter the number of terms: "))
sum_series = 0

for i in range(1, n + 1):
    term = (i ** 3) / factorial(i)
    sum_series += term

print("Sum of the series =", sum_series)
