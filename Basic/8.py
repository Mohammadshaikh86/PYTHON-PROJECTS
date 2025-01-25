import math

# Input a number
number = float(input("Enter a number: "))

# Calculate square, cube, and square root
square = number ** 2
cube = number ** 3
square_root = math.sqrt(number)

# Display results
print(f"Square of {number}: {square}")
print(f"Cube of {number}: {cube}")
print(f"Square root of {number}: {square_root:.2f}")
