# FILEPATH: /Users/bankimkamila/python120Question/Projects Mini-Projects/116.py

import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def entrance_hall():
    print_slow("You find yourself in the entrance hall of an old, mysterious house.")
    print_slow("There are three doors: one to the left, one to the right, and one straight ahead.")
    
    while True:
        choice = input("Which door do you choose? (left/right/ahead): ").lower()
        if choice == "left":
            return living_room()
        elif choice == "right":
            return kitchen()
        elif choice == "ahead":
            return study()
        else:
            print("Invalid choice. Please choose left, right, or ahead.")

def living_room():
    print_slow("You enter a dusty living room with antique furniture.")
    print_slow("You notice a shiny key on the coffee table and a locked chest in the corner.")
    
    while True:
        choice = input("Do you want to take the key, try to open the chest, or go back? (key/chest/back): ").lower()
        if choice == "key":
            print_slow("You pocket the key. It might be useful later.")
            return living_room()
        elif choice == "chest":
            print_slow("The chest is locked. You need a key to open it.")
            return living_room()
        elif choice == "back":
            return entrance_hall()
        else:
            print("Invalid choice. Please choose key, chest, or back.")

def kitchen():
    print_slow("You step into a dimly lit kitchen. There's a strange smell in the air.")
    print_slow("You see a cookbook on the counter and a closed refrigerator.")
    
    while True:
        choice = input("Do you want to read the cookbook, open the fridge, or go back? (cookbook/fridge/back): ").lower()
        if choice == "cookbook":
            print_slow("The cookbook is full of bizarre recipes. You quickly put it back.")
            return kitchen()
        elif choice == "fridge":
            print_slow("You open the fridge and a cloud of green smoke pours out. You slam it shut quickly!")
            return kitchen()
        elif choice == "back":
            return entrance_hall()
        else:
            print("Invalid choice. Please choose cookbook, fridge, or back.")

def study():
    print_slow("You enter a cozy study filled with books and a large desk.")
    print_slow("On the desk, you see a mysterious letter and an old-fashioned telephone.")
    
    while True:
        choice = input("Do you want to read the letter, use the phone, or go back? (letter/phone/back): ").lower()
        if choice == "letter":
            print_slow("The letter contains a cryptic message: 'The key to escape lies in the past.'")
            return study()
        elif choice == "phone":
            print_slow("You pick up the phone and hear a ghostly whisper: 'Find the hidden passage...'")
            return study()
        elif choice == "back":
            return entrance_hall()
        else:
            print("Invalid choice. Please choose letter, phone, or back.")

def play_game():
    print_slow("Welcome to the Mysterious House Adventure!")
    print_slow("Your goal is to explore the house and uncover its secrets.")
    print_slow("Good luck, and be careful...")
    print()
    
    current_room = entrance_hall
    while True:
        current_room = current_room()

if __name__ == "__main__":
    play_game()
