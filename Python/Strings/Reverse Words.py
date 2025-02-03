user_string = input("Enter a sentence: ")
reversed_words = ' '.join(user_string.split()[::-1])
print("Sentence with reversed words:", reversed_words)