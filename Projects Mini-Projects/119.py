# FILEPATH: /Users/bankimkamila/python120Question/Projects Mini-Projects/119.py

import requests
import textwrap

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def lookup_word(word):
    """Look up a word using the Free Dictionary API."""
    response = requests.get(f"{API_URL}{word}")
    if response.status_code == 200:
        return response.json()
    return None

def display_definitions(word, data):
    """Display the definitions of a word in a formatted manner."""
    print(f"\nDefinitions for '{word}':")
    for entry in data:
        for meaning in entry['meanings']:
            print(f"\n{meaning['partOfSpeech']}:")
            for i, definition in enumerate(meaning['definitions'], 1):
                wrapped_definition = textwrap.fill(definition['definition'], width=70, initial_indent='  ', subsequent_indent='    ')
                print(f"{i}. {wrapped_definition}")

def main():
    print("Welcome to the Command-Line Dictionary App!")
    print("Enter a word to look up its definition, or 'quit' to exit.")
    
    while True:
        word = input("\nEnter a word: ").strip().lower()
        
        if word == 'quit':
            break
        
        data = lookup_word(word)
        
        if data:
            display_definitions(word, data)
        else:
            print(f"Sorry, '{word}' not found in the dictionary.")
        
        print("\nEnter another word or 'quit' to exit.")
    
    print("Thank you for using the Dictionary App!")

if __name__ == "__main__":
    main()
