# Create a tuple
fruits = ("apple", "banana", "cherry", "date", "elderberry")

# Prompt the user for an element
element = input("Enter an element to check: ")

# Check if the element exists in the tuple
if element in fruits:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")
