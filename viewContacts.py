from loadContacts import load_contacts

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts available in the Database")
    else:
        print("\nContacts in the Database:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']},\n   E-mail Address: {contact['email']},"
                f"\n   Phone Number: {contact['phone']}, \n   Address: {contact['address']}\n")
    
