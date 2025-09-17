basic_pay=float(input("Enter the basic pay:"))
hra=0.10*basic_pay
ta=0.05*basic_pay
total_salary=basic_pay+hra+ta
print("Basic pay:",basic_pay)
print("HRA (10%):",hra)
print("TA (5%):",ta)
print("Total salary:",total_salary)
