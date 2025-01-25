# Input a positive integer
n = int(input("Enter a positive integer: "))

# Initialize sums
even_sum = 0
odd_sum = 0

# Calculate sums
for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

# Print results
print(f"Sum of even numbers from 1 to {n}: {even_sum}")
print(f"Sum of odd numbers from 1 to {n}: {odd_sum}")
