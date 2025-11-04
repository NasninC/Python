# Function to calculate Simple Interest
def simple_interest(principal, time, senior):
    if senior:
        rate = 12  # 12% for senior citizens
    else:
        rate = 10  # 10% for others
    si = (principal * rate * time) / 100
    return si

# --- Main Program ---
principal = float(input("Enter principal amount: "))
time = float(input("Enter time (in years): "))
senior = input("Is the customer a senior citizen? (yes/no): ").lower() == "yes"

interest = simple_interest(principal, time, senior)
print("Simple Interest =", interest)
