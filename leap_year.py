import calendar

# Input year from user
year = int(input("Enter a year: "))

# Check leap year using calendar module
if calendar.isleap(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
