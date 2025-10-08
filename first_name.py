names=input("Enter names seperated by space:").split()
count=0
for name in names:
  count+=name.lower().count('a')
print("Total 'a' count=",count)
