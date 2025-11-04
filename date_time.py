import time
import datetime

# a) Current date and time
current = datetime.datetime.now()
print("a) Current date and time:", current)

# b) Current Year
print("b) Current Year:", current.year)

# c) Month of the year
print("c) Month of the year:", current.month)

# d) Week number of the year
print("d) Week number of the year:", current.strftime("%U"))

# e) Weekday of the week
print("e) Weekday of the week:", current.strftime("%A"))

# f) Day of year
print("f) Day of year:", current.strftime("%j"))

# g) Day of month
print("g) Day of month:", current.day)

# h) Day of week
print("h) Day of week:", current.weekday() + 1)  # Monday = 1, Sunday = 7
