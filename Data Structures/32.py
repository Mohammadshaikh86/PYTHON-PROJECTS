# Take input from user
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]

# Find max and min
max_value = max(numbers)
min_value = min(numbers)

print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
