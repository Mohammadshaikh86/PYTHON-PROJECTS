from collections import Counter

# Input a string from the user
input_string = input("Enter a string: ")

# Count character frequency
char_frequency = Counter(input_string)

print("Character frequencies:")
for char, count in char_frequency.items():
    print(f"'{char}': {count}")
