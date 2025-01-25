def reverse_list(lst):
    lst.reverse()
    return lst

# Test the function
original_list = input("Enter a list of items separated by spaces: ").split()
reversed_list = reverse_list(original_list.copy())

print("Original list:", original_list)
print("Reversed list:", reversed_list)
