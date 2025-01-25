import math

def is_strong(num):
    return sum(math.factorial(int(digit)) for digit in str(num)) == num

number = int(input("Enter a number to check if it's a Strong number: "))
if is_strong(number):
    print(f"{number} is a Strong number.")
else:
    print(f"{number} is not a Strong number.")
