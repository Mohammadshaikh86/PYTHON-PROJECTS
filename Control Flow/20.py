# Input a positive integer
num = int(input("Enter a positive integer: "))

# Check if it's a palindrome
original_num = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = (reversed_num * 10) + digit
    num //= 10

# Print the result
if original_num == reversed_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")
