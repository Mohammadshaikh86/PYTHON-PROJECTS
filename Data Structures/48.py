def invert_dictionary(original_dict):
    # Check if all values are unique
    if len(original_dict.values()) != len(set(original_dict.values())):
        return "Cannot invert: duplicate values exist"
    
    # Invert the dictionary
    return {value: key for key, value in original_dict.items()}

# Example dictionary
original = {'a': 1, 'b': 2, 'c': 3}

# Invert the dictionary
inverted = invert_dictionary(original)

print("Original dictionary:", original)
print("Inverted dictionary:", inverted)

# Test with duplicate values
duplicate_dict = {'a': 1, 'b': 2, 'c': 2}
result = invert_dictionary(duplicate_dict)
print("Result with duplicate values:", result)
