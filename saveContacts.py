def save_contacts(contacts):
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']}=={contact['email']}"
                       f"=={contact['phone']}=={contact['address']}\n")

