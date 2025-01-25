def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    return factors

number = int(input("Enter a number to find its prime factors: "))
factors = prime_factors(number)
print(f"The prime factors of {number} are: {factors}")
