my_dict={input("Key:"):input("Value:") for _ in range(int(input("How many items?")))}
print("Ascending:",dict(sorted(my_dict.items())))
print("Descending:",dict(sorted(my_dict.items(),reverse=True)))
