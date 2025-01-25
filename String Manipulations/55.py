# Input a string from the user
input_string = input("Enter a string to remove spaces: ")

# Remove spaces
no_spaces = input_string.replace(" ", "")

print(f"Original string: '{input_string}'")
print(f"String without spaces: '{no_spaces}'")
