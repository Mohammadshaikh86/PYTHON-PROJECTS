# Input a letter from the user
letter = input("Enter a letter: ").lower()

# Check if it's a vowel or a consonant
if letter in 'aeiou':
    print(f"{letter} is a vowel.")
elif letter.isalpha():
    print(f"{letter} is a consonant.")
else:
    print("Invalid input. Please enter a letter.")
