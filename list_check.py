a=list(map(int,input("Enter first list:").split()))
b=list(map(int,input("Enter second list:").split()))
if len(a) == len(b):
  print("Same length")
else:
  print("Different length")
if sum(a) == sum(b):
  print("Same sum")
else:
  print("Different sum")
common=set(a) & set(b)
if common:
  print("Common values:",common)
else:
  print("No common values")
