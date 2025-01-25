# Create a tuple of strings
fruits = ("apple", "banana", "cherry", "date", "elderberry")

# Prompt the user for an index
index = int(input(f"Enter an index (0-{len(fruits)-1}): "))

# Print the element at that index
if 0 <= index < len(fruits):
    print(f"The element at index {index} is: {fruits[index]}")
else:
    print("Invalid index.")
