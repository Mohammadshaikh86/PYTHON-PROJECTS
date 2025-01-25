# Input a sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words and find the longest
words = sentence.split()
longest_word = max(words, key=len)

print(f"The longest word is '{longest_word}' with {len(longest_word)} characters.")
