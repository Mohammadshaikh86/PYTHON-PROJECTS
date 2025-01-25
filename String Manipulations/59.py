import string

def count_special_chars(s):
    special_chars = string.punctuation
    return sum(1 for char in s if char in special_chars)

# Input a string from the user
input_string = input("Enter a string: ")

# Count special characters
special_char_count = count_special_chars(input_string)

print(f"The string contains {special_char_count} special characters.")
