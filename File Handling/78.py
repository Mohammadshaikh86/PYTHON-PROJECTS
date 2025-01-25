user_input = input("Enter text to append to 'output.txt': ")

with open("output.txt", "a") as file:
    file.write("\n" + user_input)

print("The text has been appended to 'output.txt'.")
