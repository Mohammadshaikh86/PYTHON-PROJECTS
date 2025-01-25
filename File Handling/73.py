import shutil

source = input("Enter the source file name: ")
destination = input("Enter the destination file name: ")

try:
    shutil.copy2(source, destination)
    print(f"File '{source}' has been copied to '{destination}'.")
except FileNotFoundError:
    print(f"The source file '{source}' does not exist.")
