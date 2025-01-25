# Input a string from the user
input_string = input("Enter a string: ")

# Capitalize every word
capitalized = ' '.join(word.capitalize() for word in input_string.split())

print(f"Original: {input_string}")
print(f"Capitalized: {capitalized}")
