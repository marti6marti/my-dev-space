user_string = input("Enter the main string: ")
substring = input("Enter the substring: ")
index = user_string.find(substring)
if index != -1:
    print("Substring found at index:", index)
else:
    print("Substring not found.")