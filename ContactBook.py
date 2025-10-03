# Basic Contact Book

contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(f"{name} has been added to your contact book.")

def show_contacts():
    if contacts:
        print("\nYour Contact Book:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("Your contact book is empty.")

def remove_contact():
    name = input("Enter the name of the contact to remove: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} has been removed from your contact book.")
    else:
        print(f"No contact found with the name {name}.")

while True:
    print("\nContact Book Menu:")
    print("1. Show contacts")
    print("2. Add contact")
    print("3. Remove contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        show_contacts()
    elif choice == '2':
        add_contact()
    elif choice == '3':
        remove_contact()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
