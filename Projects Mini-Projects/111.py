import random
import string

def generate_password(length):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Combine all characters
    all_chars = lowercase + uppercase + digits + special_chars

    # Ensure the password contains at least one of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password length with random characters
    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    # Shuffle the password to randomize the order of characters
    random.shuffle(password)

    # Convert the list of characters to a string
    return ''.join(password)

# Get the desired password length from the user
while True:
    try:
        length = int(input("Enter the desired password length (minimum 8): "))
        if length < 8:
            print("Password length must be at least 8 characters.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

# Generate and print the password
password = generate_password(length)
print(f"Generated Password: {password}")
