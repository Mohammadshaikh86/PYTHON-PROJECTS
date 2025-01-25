# Create a set of names
names = {"Om", "Bankim", "Shiva", "kinjal", "Sneha", "Raj", "Rajesh"}

# Print the set of names
print("Set of names:", names)

# Prompt the user for a name
name = input("Enter a name to check: ")

# Check if the name is in the set
if name in names:
    print(f"{name} is in the set.")
else:
    print(f"{name} is not in the set.")
