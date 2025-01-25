# Input a non-negative integer
n = int(input("Enter a non-negative integer: "))

# Calculate factorial
factorial = 1
for i in range(1, n + 1):
    factorial *= i

# Print the result
print(f"The factorial of {n} is: {factorial}")
