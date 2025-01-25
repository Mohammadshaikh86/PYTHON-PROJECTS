# Prompt the user for input
user_input = input("Enter a string to write to the file: ")

# Write to file
with open("output.txt", "w") as file:
    file.write(user_input)

print("The string has been written to 'output.txt'.")
