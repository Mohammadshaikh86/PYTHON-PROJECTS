def is_perfect(num):
    return sum(i for i in range(1, num) if num % i == 0) == num

number = int(input("Enter a number to check if it's a Perfect number: "))
if is_perfect(number):
    print(f"{number} is a Perfect number.")
else:
    print(f"{number} is not a Perfect number.")
