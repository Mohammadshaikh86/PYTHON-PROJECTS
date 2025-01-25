filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        longest_line = max(file, key=len)
    print(f"The longest line in '{filename}' is:")
    print(longest_line.strip())
except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")
