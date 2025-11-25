import json
import os

# Load contacts if file exists
if os.path.exists('contacts.json'):
    with open('contacts.json', 'r') as f:
        contacts = json.load(f)
else:
    contacts = {}

while True:
    print('\n===== Contact Book App =====')
    print('1. Create contact')
    print('2. View contact')
    print('3. Update contact')
    print('4. Delete contact')
    print('5. Search contact')
    print('6. Total contacts')
    print('7. View all contacts')
    print('8. Exit')

    choice = input('Enter your choice = ')

    # 1️⃣ Create contact
    if choice == '1':
        name = input('Enter name = ').strip()
        if name in contacts:
            print(f'Contact name "{name}" already exists!')
        else:
            try:
                age = int(input('Enter age = '))
            except ValueError:
                print('Invalid age! Please enter a number.')
                continue

            email = input('Enter email = ').strip()
            mobile = input('Enter mobile number = ').strip()

            contacts[name] = {'age': age, 'email': email, 'mobile': mobile}
            print(f'Contact "{name}" has been created successfully!')

    # 2️⃣ View single contact
    elif choice == '2':
        name = input('Enter contact name to view = ').strip()
        if name in contacts:
            c = contacts[name]
            print(f'''
--- Contact Info ---
Name   : {name}
Age    : {c["age"]}
Email  : {c["email"]}
Mobile : {c["mobile"]}
---------------------
''')
        else:
            print('Contact not found!')

    # 3️⃣ Update contact
    elif choice == '3':
        name = input('Enter name to update contact = ').strip()
        if name in contacts:
            try:
                age = int(input('Enter updated age = '))
            except ValueError:
                print('Invalid age! Please enter a number.')
                continue

            email = input('Enter updated email = ').strip()
            mobile = input('Enter updated mobile number = ').strip()

            contacts[name] = {'age': age, 'email': email, 'mobile': mobile}
            print(f'Contact "{name}" updated successfully!')
        else:
            print('Contact not found!')

    # 4️⃣ Delete contact
    elif choice == '4':
        name = input('Enter contact name to delete = ').strip()
        if name in contacts:
            del contacts[name]
            print(f'Contact "{name}" deleted successfully!')
        else:
            print('Contact not found!')

    # 5️⃣ Search contact
    elif choice == '5':
        search_name = input('Enter contact name to search = ').strip()
        found = False
        for name, c in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found - Name: {name}, Age: {c["age"]}, Email: {c["email"]}, Mobile: {c["mobile"]}')
                found = True
        if not found:
            print('No contact found with that name!')

    # 6️⃣ Show total count
    elif choice == '6':
        print(f'Total contacts in your book: {len(contacts)}')

    # 7️⃣ View all contacts
    elif choice == '7':
        if contacts:
            print('\n--- All Contacts ---')
            for name, c in contacts.items():
                print(f'Name: {name}, Age: {c["age"]}, Email: {c["email"]}, Mobile: {c["mobile"]}')
        else:
            print('No contacts available!')

    # 8️⃣ Exit & Save
    elif choice == '8':
        with open('contacts.json', 'w') as f:
            json.dump(contacts, f, indent=4)
        print('Contacts saved successfully! Goodbye 👋')
        break

    else:
        print('Invalid input! Please try again.')
