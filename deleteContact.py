from loadContacts import load_contacts
from saveContacts import save_contacts

def delete_contact():
    contacts = load_contacts()
    name_to_delete=input("The name you want to delete is: ")

    found_contacts = [contact for contact in contacts
                        if contact["name"] == name_to_delete]

    updated_contacts = [contact for contact in contacts
                        if contact["name"] != name_to_delete]
    if len(updated_contacts)!=0:
        save_contacts(updated_contacts)
        contacts.clear()
        contacts.extend(updated_contacts)

        print(f"Contact '{name_to_delete}' (associated with {len(found_contacts)} no. contact(s))"
              f" has been deleted.\n")
    else: print("Nothing to delete!!!\n")
