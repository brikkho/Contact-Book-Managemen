def load_contacts():
    contacts = []
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, email, phone, address = line.strip().split("==")
                contacts.append({
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "address": address,
                    })
    except: pass
    
    return contacts
    
