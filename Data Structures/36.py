# Prompt for a list of integers
numbers = input("Enter a list of integers (possibly with duplicates) separated by spaces: ").split()
numbers = [int(num) for num in numbers]

# Remove duplicates
unique_numbers = list(dict.fromkeys(numbers))

print("Original list:", numbers)
print("List with duplicates removed:", unique_numbers)
