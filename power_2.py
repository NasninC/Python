# Display powers of 2 using lambda and map
n = int(input("Enter number of terms: "))
powers = list(map(lambda x: 2 ** x, range(n)))
print("Powers of 2:", powers)
