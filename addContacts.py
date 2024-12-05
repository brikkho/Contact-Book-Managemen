from loadContacts import load_contacts
from searchContact import search_phone
from saveContacts import save_contacts

def add_contacts():
    contacts = load_contacts()
    
    name = input("Enter the Name: ")
    email = input(f"Enter E-mail address of {name}: ")
    phone = input(f"Enter Phone Number of {name}: ")
    while not phone.isdigit() or len(phone) < 11:
        print("Invalid phone number. Ensure it contains only digits, and is 11 characters long.")
        phone = input(f"Enter Phone Number of {name}: ")
        
    if any(contact['phone'] == phone for contact in contacts):
        print(
            f"Error: This phone number is already associated with another contact.\n"
            f"Contact '{name}' could not be added."
        )
        return
    
    address = input("Enter the Address: ")
    person = {
    "name": name,
    "email": email,
    "phone": phone,
    "address": address}

    contacts.append(person)  
    save_contacts(contacts)  
    print(f"\nContact '{name}' added successfully!\n")

