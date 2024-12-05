from loadContacts import load_contacts

def search_name():
    contacts = load_contacts()
    try: name_to_search = name
    except: name_to_search = input("Enter the name you want to search: ")

    found_contacts = [contact for contact in contacts
                        if contact["name"] == name_to_search]
    if len(found_contacts)!=0:
        print(f"'{name_to_search}' has been found {len(found_contacts)} time(s).")
        print(f"Found contacts associated with the name- '{name_to_search}' is (are):\n")
        
        for contact in found_contacts:
            i=found_contacts.index(contact)
            print(f"{i+1}. {contact}\n")
            
    else:
        print(f"\nNot Found any contact named: '{name_to_search}'")
        print("However, you are requested to search a contact by Full Name. \nThank You.\n")
    
def search_phone():
    contacts = load_contacts()
    try: phone_to_search = phone
    except: phone_to_search = input("Enter the Phone Number you want to search: ")

    found_contacts = [contact for contact in contacts
                        if contact["phone"] == phone_to_search]
    
    if len(found_contacts)!=0:
        return True
    else:
        return False

def search_email():
    contacts = load_contacts()
    try: email_to_search = email
    except: email_to_search = input("Enter the Email Address you want to search: ")

    found_contacts = [contact for contact in contacts
                        if contact["email"] == email_to_search]

    if len(found_contacts)!=0:
        print(f"'{email_to_search}' has been found {len(found_contacts)} time(s).")
   
