# Prompt the user for two variables
var1 = input("Enter the first variable: ")
var2 = input("Enter the second variable: ")

# Display values before swapping
print("\nBefore swapping:")
print(f"First variable: {var1}")
print(f"Second variable: {var2}")

# Swap the values
var1, var2 = var2, var1

# Display values after swapping
print("\nAfter swapping:")
print(f"First variable: {var1}")
print(f"Second variable: {var2}")
