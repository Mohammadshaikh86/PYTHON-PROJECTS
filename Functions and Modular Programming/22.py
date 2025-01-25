def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Test the function
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = power(base, exponent)
print(f"{base}^{exponent} = {result}")
