start=int(input("Enter starting number:"))
end=int(input("Enter ending number:"))
print("Four digits numbers with all even digits and perfect square:")
for num in range(start,end+1):
    if num>=1000 and num<=9999:
        if all(int(d)%2 == 0 for d in str(num)):
            if int(num**0.5)**2==num:
                print(num)
