try:
    with open("output.txt", "r") as file:
        content = file.read()
        print("Content of 'output.txt':")
        print(content)
except FileNotFoundError:
    print("The file 'output.txt' does not exist.")
