user_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in user_string if char in vowels)
print("Number of vowels:", count)
