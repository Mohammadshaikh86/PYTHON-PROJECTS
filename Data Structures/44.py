def word_count(string):
    words = string.lower().split()
    return {word: words.count(word) for word in set(words)}

# Prompt the user for a string
input_string = input("Enter a string: ")

# Count words
result = word_count(input_string)
print("Word count:", result)
