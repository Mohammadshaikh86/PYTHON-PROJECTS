decimal = int(input("Enter a decimal number: "))
binary = bin(decimal)[2:]  # [2:] to remove the '0b' prefix
print(f"The binary equivalent of {decimal} is {binary}.")
