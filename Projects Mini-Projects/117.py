# FILEPATH: /Users/bankimkamila/python120Question/Projects Mini-Projects/117.py

import random

def get_player_choice():
    """Get the player's choice of rock, paper, or scissors."""
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    """Determine the winner based on the choices."""
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Play a single round of Rock-Paper-Scissors."""
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(player_choice, computer_choice)
    print(result)
    
    return result

def main():
    print("Welcome to Rock-Paper-Scissors!")
    player_score = 0
    computer_score = 0
    ties = 0
    
    while True:
        result = play_game()
        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        else:
            ties += 1
        
        print(f"\nScore - You: {player_score}, Computer: {computer_score}, Ties: {ties}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print("\nFinal Score:")
    print(f"You: {player_score}")
    print(f"Computer: {computer_score}")
    print(f"Ties: {ties}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
