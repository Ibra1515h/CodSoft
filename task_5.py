import re

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone}")

    def search_contact(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, index, name, phone, email, address):
        if 0 <= index < len(self.contacts):
            contact = self.contacts[index]
            contact.name = name
            contact.phone = phone
            contact.email = email
            contact.address = address
            print(f"Contact {name} updated successfully!")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            contact = self.contacts.pop(index)
            print(f"Contact {contact.name} deleted successfully!")
        else:
            print("Invalid contact index.")

def validate_email(email):
    if '@' in email and len(email) >= 5:
        return True
    return False

def validate_phone(phone):
    # Regex pattern for phone number: +CountryCode-10digits
    pattern = r'^\+\d{1,4}-\d{10}$'
    if re.match(pattern, phone):
        return True
    return False

def get_valid_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        print("Invalid input. Please try again.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = get_valid_input("Enter phone number (format: +CountryCode-10digits): ", validate_phone)
            email = get_valid_input("Enter email: ", validate_email)
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_manager.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            results = contact_manager.search_contact(query)
            if results:
                print("\nSearch Results:")
                for i, contact in enumerate(results, 1):
                    print(f"{i}. {contact.name} - {contact.phone}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            contact_manager.view_contacts()
            try:
                index = int(input("Enter the index of the contact to update: ")) - 1
                name = input("Enter new name: ")
                phone = get_valid_input("Enter new phone number (format: +CountryCode-10digits): ", validate_phone)
                email = get_valid_input("Enter new email: ", validate_email)
                address = input("Enter new address: ")
                contact_manager.update_contact(index, name, phone, email, address)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == '5':
            contact_manager.view_contacts()
            try:
                index = int(input("Enter the index of the contact to delete: ")) - 1
                contact_manager.delete_contact(index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == '6':
            print("Thank you for using the Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

