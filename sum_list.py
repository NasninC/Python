numbers=list(map(int,input("Enter numbers seperated by spaces:").split()))
total = 0
for num in numbers:
    total += num
print("Sum of all items in the list=",total)
