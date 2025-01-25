filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        lines = content.split("\n")
        words = content.split()
        characters = len(content)
        
    print(f"File Statistics for '{filename}':")
    print(f"Total characters: {characters}")
    print(f"Total lines: {len(lines)}")
    print(f"Total words: {len(words)}")
    print(f"Average characters per line: {characters / len(lines):.2f}")
    print(f"Average words per line: {len(words) / len(lines):.2f}")
except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")
