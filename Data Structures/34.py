# Prompt for a list of numbers
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]

# Calculate sum and average
sum_of_numbers = sum(numbers)
average = sum_of_numbers / len(numbers)

print(f"Sum: {sum_of_numbers}")
print(f"Average: {average}")
