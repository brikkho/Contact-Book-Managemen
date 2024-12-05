from loadContacts import load_contacts
from addContacts import add_contacts
from deleteContact import delete_contact
from saveContacts import save_contacts
from searchContact import search_name
from viewContacts import view_contacts


def main_menu():
    print("----------Contact Book Management System----------")
    print("***************************************************")
    print("1. Add a Contact")
    print("2. View All Contacts")
    print("3. Delete a contact")
    print("4. Search a contact")
    print("0. Exit\n")
    
    choice = input("Enter your choice: ")
    return choice

def main():
    while True:
        choice = main_menu()
        if choice == "1": add_contacts()
        elif choice == "2": view_contacts()
        elif choice == "3": delete_contact()
        elif choice == "4": search_name()
            
        elif choice == "0":
            print("Exiting the Contact Book Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
