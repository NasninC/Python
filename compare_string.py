def compare(S1, S2, n):
    return S1[:n] == S2[:n]

# Main program
S1 = input("Enter first string: ")
S2 = input("Enter second string: ")
n = int(input("Enter number of characters to compare: "))

if compare(S1, S2, n):
    print("Same")
else:
    print("Different")
