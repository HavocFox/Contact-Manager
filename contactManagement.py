import re
contacts = {
    '1234567890': {'Name': 'Mathew McConaughey', 'Email': 'crungus@gmail.com', 'Phone': '1234567890'},
    '2234567890': {'Name': '1Mathew McConaughey', 'Email': '1crungus@gmail.com', 'Phone': '2234567890'},
    '3234567890': {'Name': '2Mathew McConaughey', 'Email': '2crungus@gmail.com', 'Phone': '3234567890'},
    '4234567890': {'Name': '3Mathew McConaughey', 'Email': '3crungus@gmail.com', 'Phone': '4234567890'},
}


#--------------------------------------------------------

def contact_add():
    duplicate = False
    while True:
        try:
            while True:
                identifier = input("What is the phone number you are entering contact information for? This will serve as an identifier: ")
                if len(identifier) == 10:
                    break
                else:
                    print("Please enter a valid 10-digit phone number (Without hyphens, including area code). ")
        except ValueError:
            print("Please enter a valid phone number. ")
        else:
            break

    for contact, info in contacts.items():
        if identifier in info['Phone']:
            print("You cannot enter a duplicate contact. ")
            return


    name = input("What is the name of this contact? ")
    phone = identifier

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    while True:
        email = input("What is their email address? ").lower()
        if not (re.match(pattern, email)):
            print("Please enter a valid email. ")

        for contact, info in contacts.items():
            if email in info['Email']:
                print("You cannot enter a duplicate contact. ")
                duplicate = True

        if not duplicate:
            break
        duplicate = False

    contacts[identifier] = {"Name" : name, "Email" : email, "Phone" : phone}

    print(f"The following contact has been added: {contacts[identifier]}\n")

#--------------------------------------------------------

def contact_display():
    print("\nYour contacts: ")
    for contact, info in contacts.items():
        print(f'Identifier (Phone or Email): {contact} Name: {info['Name']} Email: {info['Email']} Phone #:  {info['Phone']}\n')

#--------------------------------------------------------

def contact_edit():
    search_term = input("Which contact do you want to edit? Please enter its identifier. ")

    for contact, info in contacts.items():
        if search_term in contact:
            print("This is the contact you are editing: ")
            print(f'Identifier (Phone): {contact} Name: {info['Name']} Email: {info['Email']} Phone #: {info['Phone']}\n')

    edit_choice = input("What part of the contact would you like to edit? Name, Email or Phone? ").lower()
    if edit_choice == 'name':
        new_value = input("Please enter the new name: ")
        contacts[search_term]['Name'] = new_value
        print(f"Name updated to {new_value}.\n")

    if edit_choice == 'email':
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        while True:
            new_value = input("Please enter the new email: ")
            if re.match(pattern, new_value):
                contacts[search_term]['Email'] = new_value
                print(f"Email updated to {new_value}.\n")
                break
            else:
                print("Please enter a valid email. ")

    if edit_choice == 'phone':
        while True:
            try:
                new_value = int(input("Please enter the new phone number: "))
                if new_value > 1000000000:
                    break
                else:
                    print("Please enter a valid phone number.")
            except ValueError:
                print("Please enter a valid phone number.")
            else:
                break

        contacts[new_value] = contacts.pop(search_term)
        contacts[new_value]['Phone'] = new_value
        print(f"Phone # updated to {new_value}.\n")

#--------------------------------------------------------

def contact_search():
    print("Please enter the identifier of the contact you're searching for. ")
    search_term = input("This would be a phone number or email address. ")

    for contact, info in contacts.items():
        if search_term in contact:
            print("Found! ")
            print("The contact that was found: ")
            print(f'Identifier (Phone): {contact} Name: {info['Name']} Email: {info['Email']} Phone #: {info['Phone']}\n')

#--------------------------------------------------------

def contact_export():
    print("Exporting contacts...")
    with open('contacts_exported.txt', 'w') as file:
        if file:
            ovchoice = input("There is already an exported contacts file. Would you like to overwrite it? Y or N ").upper()

            if ovchoice == 'Y' or not ovchoice:
                for contact, info in contacts.items():
                    file.write(f'Identifier): {contact} Name: {info['Name']} Email: {info['Email']} Phone #: {info['Phone']}\n')
                print("success")
            else:
                ("Returning to menu. \n")
            
    file.close()

#--------------------------------------------------------

def contact_import():
    
    while True:
        try:
            file_to_open = input("What is the name of the file you are importing contacts from? ")      # Might need error handling for weird characters entered
            with open(file_to_open, 'r') as file:
                for line in file:
                    info = line.strip().split(',')  # Split the line into contact info
                    phone = info[0]
                    name = info[1]
                    email = info[2]
                    contacts[phone] = {'Name': name, 'Email': email, 'Phone': phone}  # Add contact to dictionary
                    
        except FileNotFoundError:
            print("That file does not exist! ")
            
        else:
            break

    print("Contacts imported successfully. \n")



#--------------------------------------------------------

user_choice = 0

print("Welcome to the Contact Management System!")
while True:

    print('\nMenu: \n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Import contacts from a text file\n8. Quit')
    try:
         user_choice = int(input("\nWhat would you like to do? Please enter the number of your selection.  "))
    except ValueError:
        print("Please enter a valid number.\n")

    if user_choice == 1:
        print("You have chosen to add a new contact. ")
        contact_add()

    if user_choice == 2:
        if len(contacts) == 0:
            print("There's nothing in your contacts.")
        else:
            print("You have chosen to edit a contact. ")
            contact_edit()

    if user_choice == 3:
        if len(contacts) == 0:
            print("There's nothing in your contacts.")
        else:
            print("You have chosen to delete a contact. ")

    if user_choice == 4:
        if len(contacts) == 0:
            print("There's nothing in your contacts.")
        else:
            print("You have chosen to search for a contact. ")
            contact_search()

    if user_choice == 5:
        if len(contacts) == 0:
            print("There's nothing in your contacts.")
        else:
            print("You have chosen to view your contacts. ")
            contact_display()

    if user_choice == 6:
        if len(contacts) == 0:
            print("There's nothing in your contacts.")
        else:
            print("You have chosen to export your contacts to a text file. ")
            contact_export()

    if user_choice == 7:
        print("You have chosen to import contacts from a text file. ")
        contact_import()

    if user_choice == 8:
        print("Thank you for using the Contact Management System.\n ")
        break