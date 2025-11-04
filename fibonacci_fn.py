def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# Main program
n = int(input("Enter number of terms: "))

print("Fibonacci Series:")
for i in range(n):
    print(fib(i), end=" ")
