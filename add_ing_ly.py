text=input("Enter a string:")
if text.endswith("ing"):
 text=text+"ly"
else:
 text=text+"ing"
print("MOdified string:",text)
