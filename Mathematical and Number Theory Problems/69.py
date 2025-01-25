import math

def lcm_range(n):
    lcm = 1
    for i in range(1, n + 1):
        lcm = (lcm * i) // math.gcd(lcm, i)
    return lcm

n = int(input("Enter the upper limit of the range (1 to n) to compute LCM: "))
result = lcm_range(n)
print(f"The LCM of numbers from 1 to {n} is {result}")
