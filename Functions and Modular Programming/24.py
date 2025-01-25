def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(f"{num} is prime.")
else:
    print(f"{num} is not prime.")
