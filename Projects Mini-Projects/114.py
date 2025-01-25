import random

# List of words to choose from
words = ["python", "programming", "computer", "science", "algorithm", "database", "network", "software", "developer"]

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    word = choose_word()
    word_letters = set(word)  # letters in the word
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    guessed_letters = set()  # letters guessed by the player

    lives = 6  # number of lives

    # Game loop
    while len(word_letters) > 0 and lives > 0:
        print("\nYou have", lives, "lives left.")
        print("Guessed letters:", ' '.join(guessed_letters))

        # Display the word with guessed letters
        word_list = [letter if letter in guessed_letters else '_' for letter in word]
        print("Current word:", ' '.join(word_list))

        guess = input("Guess a letter: ").lower()
        if guess in alphabet - guessed_letters:
            guessed_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                lives = lives - 1
                print("Letter is not in the word.")
        elif guess in guessed_letters:
            print("You have already guessed that letter. Try again!")
        else:
            print("Invalid character. Please enter a letter.")

    # Game ended
    if lives == 0:
        print("\nSorry, you died. The word was", word)
    else:
        print("\nCongratulations! You guessed the word", word, "!!")

# Main game loop
while True:
    hangman()
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        break

print("Thanks for playing Hangman!")
