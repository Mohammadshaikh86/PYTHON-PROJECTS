def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

number = int(input("Enter a number to compute the sum of its digits: "))
digit_sum = sum_of_digits(number)
print(f"The sum of digits of {number} is {digit_sum}.")
