filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        word_count = len(content.split())
    print(f"The file '{filename}' contains {word_count} words.")
except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")
