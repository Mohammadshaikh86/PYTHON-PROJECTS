# Prompt for a list of integers
numbers = input("Enter a list of integers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

positive = sum(1 for num in numbers if num > 0)
negative = sum(1 for num in numbers if num < 0)
zero = sum(1 for num in numbers if num == 0)

print(f"Positive numbers: {positive}")
print(f"Negative numbers: {negative}")
print(f"Zeros: {zero}")
