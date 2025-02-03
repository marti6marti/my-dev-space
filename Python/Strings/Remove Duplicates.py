user_string = input("Enter a string: ")
result = ''.join(dict.fromkeys(user_string))
print("String without duplicates:", result)
