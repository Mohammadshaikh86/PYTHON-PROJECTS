# Input a positive integer
num = int(input("Enter a positive integer: "))

# Reverse the number
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = (reversed_num * 10) + digit
    num //= 10

# Print the result
print(f"The reversed number is: {reversed_num}")
