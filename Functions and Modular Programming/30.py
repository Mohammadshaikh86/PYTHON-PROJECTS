def count_occurrences(lst, x):
    return lst.count(x)

# Test the function
input_list = input("Enter a list of elements separated by spaces: ").split()
element = input("Enter the element to count: ")
occurrences = count_occurrences(input_list, element)
print(f"The element '{element}' appears {occurrences} times in the list.")
