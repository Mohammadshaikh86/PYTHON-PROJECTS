def second_largest(numbers):
    unique_sorted = sorted(set(numbers), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None

# Take input from user
numbers = input("Enter a list of unique integers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

result = second_largest(numbers)
if result is not None:
    print(f"The second largest element is: {result}")
else:
    print("There is no second largest element.")
