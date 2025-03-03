def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return [i for i in range(2, n+1) if primes[i]]

n = int(input("Enter a number to find all primes up to that number: "))
primes = sieve_of_eratosthenes(n)
print(f"Prime numbers up to {n}: {primes}")
