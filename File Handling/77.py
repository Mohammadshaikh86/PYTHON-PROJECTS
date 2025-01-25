filename = input("Enter the file name: ")
search_word = input("Enter the word to search for: ")

try:
    with open(filename, "r") as file:
        for line_number, line in enumerate(file, 1):
            if search_word in line:
                print(f"Found '{search_word}' on line {line_number}: {line.strip()}")
except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")
