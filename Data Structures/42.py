# Create a tuple
original_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", original_tuple)

# Convert tuple to list
temp_list = list(original_tuple)

# Modify the list
temp_list[4] = 90

# Convert back to tuple
new_tuple = tuple(temp_list)

print("Modified tuple:", new_tuple)
