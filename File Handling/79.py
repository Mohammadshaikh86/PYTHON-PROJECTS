input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")

try:
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            if line.strip():
                outfile.write(line)
    print(f"Non-blank lines have been written to '{output_file}'.")
except FileNotFoundError:
    print(f"The input file '{input_file}' does not exist.")
