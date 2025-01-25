# Function to convert string input to set
def input_to_set(prompt):
    return set(input(prompt).split())

# Get input from user
set1 = input_to_set("Enter elements for the first set (space-separated): ")
set2 = input_to_set("Enter elements for the second set (space-separated): ")

# Perform set operations
union = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1.difference(set2)

# Display results
print("Union:", union)
print("Intersection:", intersection)
print("Difference (set1 - set2):", difference)
