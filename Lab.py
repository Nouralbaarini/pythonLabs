
def main(contacts=[("Stish", "123"), 
                   ("Rita", "321")]):
    while True:
        print("\nContact App Menu:")
        print("v - View Contacts")
        print("a - Add Contact")
        print("d - Delete Contact")
        print("q - Quit")
        
        choice = input("Enter choice(v,a,d,q- to quit): ").lower()
        
        if choice == 'v':
           view_contacts(contacts)
        elif choice == 'a':
           contacts = add_contact(contacts)
        elif choice == 'd':
           contacts = delete_contact(contacts)
        elif choice == 'q':
           print("------ goodbye ------")
           break
        else:
           print("------ Invalid option! Please try again. ------")
           
def view_contacts(contacts):
    print("*****    Contact List    *****")
    if len(contacts) == 0:
        print("No contacts available.")
    else:
        for index, (name, number) in enumerate(contacts, start=1):
            print(f"{index}. {name}: {number}")


def add_contact(contacts):
    print("*****    Add Contact    *****")
    name = input("Enter the name of the new contact: ")
    number = input("Enter the phone number of the new contact: ")
    contacts.append((name, number))
    print(f"Contact {name} added successfully.")
    return contacts

def delete_contact(contacts):
    view_contacts(contacts)
    if len(contacts) == 0:
       return contacts
    contact_number = input("Enter the number of the contact to delete: ")
    try: 
        index = int(contact_number)-1 
        if index < 0 or index >= len(contacts):
            print("Invalid contact number")
        else:
            removed_contact = contacts.pop(index)
            print(f"Contact {removed_contact[0]} deleted successfully.")
    except ValueError:
        print("Please enter a valid number.")
    return contacts

if __name__ == "__main__":
    main()
