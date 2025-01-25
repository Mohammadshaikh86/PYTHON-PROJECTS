# Input two lists from the user
list1 = input("Enter the first list of numbers separated by spaces: ").split()
list2 = input("Enter the second list of numbers separated by spaces: ").split()

# Convert to integers
list1 = [int(num) for num in list1]
list2 = [int(num) for num in list2]

# Ensure lists are of equal length
if len(list1) != len(list2):
    print("Error: Lists must be of equal length.")
else:
    # Calculate element-wise sum
    sum_list = [a + b for a, b in zip(list1, list2)]
    print("Element-wise sum:", sum_list)
