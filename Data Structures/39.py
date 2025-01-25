# Input two lists from the user
list1 = input("Enter the first list of items separated by spaces: ").split()
list2 = input("Enter the second list of items separated by spaces: ").split()

# Find common elements
common_elements = list(set(list1) & set(list2))

print("Common elements:", common_elements)
