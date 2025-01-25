# FILEPATH: /Users/bankimkamila/python120Question/Projects Mini-Projects/118.py

import re

def validate_email(email):
    """Validate the email address using a simple regex pattern."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def slice_email(email):
    """Slice the email address into username and domain."""
    username, domain = email.split('@')
    return username, domain

def main():
    print("Welcome to the Email Slicer!")
    
    while True:
        email = input("Please enter an email address: ").strip()
        
        if validate_email(email):
            username, domain = slice_email(email)
            print(f"\nUsername: {username}")
            print(f"Domain: {domain}")
            
            # Extract the top-level domain
            tld = domain.split('.')[-1]
            print(f"Top-Level Domain: {tld}")
            
            break
        else:
            print("Invalid email address. Please try again.")
    
    print("\nThank you for using the Email Slicer!")

if __name__ == "__main__":
    main()
