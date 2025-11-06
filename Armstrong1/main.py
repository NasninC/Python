import Armstrong1
lower=int(input("Enter lower limit:"))
upper=int(input("Enter upper limit:"))
print(f"Armstrong numbers between {lower} and {upper} are:")
for num in range(lower,upper+1):
    if Armstrong1.is_armstrong(num):
        print(num)

