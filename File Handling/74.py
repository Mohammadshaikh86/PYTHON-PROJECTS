filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        line_count = sum(1 for line in file)
    print(f"The file '{filename}' contains {line_count} lines.")
except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")
