import csv
import os

# File to store contacts
CONTACTS_FILE = "contacts.csv"

def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            reader = csv.reader(file)
            contacts = list(reader)
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

def add_contact(contacts):
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts.append([name, number, email])
    save_contacts(contacts)
    print("Contact added successfully!")

def search_contact(contacts):
    search_term = input("Enter name or number to search: ").lower()
    found_contacts = []
    for contact in contacts:
        if search_term in contact[0].lower() or search_term in contact[1]:
            found_contacts.append(contact)
    
    if found_contacts:
        print("\nFound contacts:")
        for contact in found_contacts:
            print(f"Name: {contact[0]}, Number: {contact[1]}, Email: {contact[2]}")
    else:
        print("No contacts found.")

def display_menu():
    print("\nContact Book Menu:")
    print("1. Add a new contact")
    print("2. Search for a contact")
    print("3. Exit")

def main():
    contacts = load_contacts()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            print("Thank you for using the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
