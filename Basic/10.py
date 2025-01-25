# Input principal, rate, and time
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in percentage): "))
time = float(input("Enter the time period (in years): "))

# Compute simple interest
simple_interest = (principal * rate * time) / 100

# Display the result
print(f"The simple interest is: {simple_interest:.2f}")
