text=input("Enter a string:")
first_char=text[0]
new_text=first_char + text[1:].replace(first_char,'$')
print("Result:",new_text)
