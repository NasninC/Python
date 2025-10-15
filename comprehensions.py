numbers=list(map(int,input("Enter integers seperated by spaces:").split()))
positive_list=[x for x in numbers if x>0]
print("(a) Positive numbers:",positive_list)
square_list=[x**2 for x in numbers]
print("(b) Squares:",square_list)
word=input("Enter a word:")
vowels='aeiouAEIOU'
vowel_list=[ch for ch in word if ch in vowels]
print("(c) Vowels:",vowel_list)
ordinal_list=[ord(ch) for ch in word]
print("(d) Ordinal values:",ordinal_list)
