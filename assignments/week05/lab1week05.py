
def contact_book():
    """
    Contact management system using dictionaries
    Each contact: {"name": str, "phone": str, "email": str, "category": str}
    """
    
    # Initialize empty contacts dictionary
    # Key: contact name (string), Value: contact info (dictionary)
    contacts = {
        "John Doe": {"phone": "123-456-7890", "email": "john@example.com", "category": "friend"},
        "Jane Smith": {"phone": "987-654-3210", "email": "jane@example.com", "category": "work"},
    }
    
    def add_contact():
        """Add a new contact to the address book"""
        print("\n=== Add New Contact ===")
        
        # Get contact information from user
        name = input("Enter contact name: ").strip()
        
        # TODO: Check if contact already exists
        # If exists, ask user if they want to update
        if name in contacts:    
            print(f"Contact '{name}' already exists.")
            choice = input("Do you want to update it? (y/n): ").strip().lower()
            if choice != 'y':
                return
        
        phone = input("Enter phone number: ").strip()
        email = input("Enter email address: ").strip()
        category = input("Enter category (family/friend/work/other): ").strip().lower()
        
        # TODO: Create contact dictionary and add to contacts
        contact_info = {    
            "phone": phone,
            "email": email,
            "category": category
            # Fill in the contact information
        }
        # TODO: Add contact to the contacts dictionary
        contacts[name] = contact_info
        print(f"Contact '{name}' added successfully!")
    
    def view_contact():
        """View details of a specific contact"""
        print("\n=== View Contact ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        name = input("Enter contact name to view: ").strip()
        
        # TODO: Check if contact exists and display information
        # Format the output nicely
        if name in contacts:
            info = contacts[name]
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Category: {info['category']}")
        else:
            print(f"Contact '{name}' not found.")
        pass
    
    def search_contacts():
        """Search contacts by name, phone, or email"""
        print("\n=== Search Contacts ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        search_term = input("Enter search term (name/phone/email): ").strip().lower()
        
        # TODO: Search through all contacts
        # Check if search term appears in name, phone, or email
        # Display all matching contacts
        
        found_contacts = []
        
        # TODO: Implement search logic
        for name, info in contacts.items():
            if (search_term in name.lower() or
                search_term in info["phone"].lower() or
                search_term in info["email"].lower()):
                found_contacts.append((name, info))

        if found_contacts:
            print(f"\nFound {len(found_contacts)} contact(s):")
            # TODO: Display found contacts
            for name, info in found_contacts:
                print(f"- {name}: {info['phone']}, {info['email']}, {info['category']}")
        
        if found_contacts:
            print(f"\nFound {len(found_contacts)} contact(s):")
            # TODO: Display found contacts
        else:
            print("No contacts found matching your search.")
    
    def list_all_contacts():
        """Display all contacts in a formatted way"""
        print("\n=== All Contacts ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        print(f"{'Name':<20} {'Phone':<15} {'Email':<25} {'Category':<10}")
        print("-" * 70)
        
        # TODO: Implement listing logic
        for name, info in contacts.items():
            print(f"{name:<20} {info['phone']:<15} {info['email']:<25} {info['category']:<10}")
        pass
    
    def update_contact():
        """Update an existing contact"""
        print("\n=== Update Contact ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        name = input("Enter contact name to update: ").strip()
        
        # TODO: Check if contact exists
        if name not in contacts:
            print(f"Contact '{name}' not found.")
            return
        # If exists, show current information
        print(f"Current info: {contacts[name]}")
        # Ask what field to update
        field = input("Which field do you want to update? (phone/email/category): ").strip().lower()
        if field not in ['phone', 'email', 'category']:
            print("Invalid field.")
            return
        # Update the contact information
        new_value = input(f"Enter new {field}: ").strip()
        contacts[name][field] = new_value
        print(f"{field.capitalize()} updated successfully.")
        
        pass
    
    def delete_contact():
        """Delete a contact"""
        print("\n=== Delete Contact ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        name = input("Enter contact name to delete: ").strip()
        
        # TODO: Check if contact exists
        if name not in contacts:
            print(f"Contact '{name}' not found.")
            return
        # Ask for confirmation
        confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").strip().lower()
        if confirm == 'y':
            # Delete the contact
            del contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print("Deletion cancelled.")
    
    # Main menu loop
    while True:
        print("\n" + "="*50)
        print("           CONTACT BOOK MANAGER")
        print("="*50)
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search Contacts")
        print("4. List All Contacts")
        print("5. Update Contact")
        print("6. Delete Contact")
        print("7. Exit")
        print("-"*50)
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            list_all_contacts()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            delete_contact()
        elif choice == "7":
            print("Thank you for using Contact Book Manager!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-7.")

if __name__ == "__main__":
    print("Starting Contact Book Manager...")
    
    contact_book()