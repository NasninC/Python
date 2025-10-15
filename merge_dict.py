dict1= {}
dict1[int(input("Enter key for dict1:"))]=input("Enter value:")
dict2= {}
dict2[int(input("Enter key for dict2:"))]=input("Enter value:")
dict1.update(dict2)
print("Merged dictionary:",dict1)
