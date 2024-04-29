contacts = {
    '1234567890': {'Name': 'Mathew McConaughey', 'Email': 'crungus@gmail.com', 'Phone': '1234567890'},
    '2234567890': {'Name': '1Mathew McConaughey', 'Email': '1crungus@gmail.com', 'Phone': '2234567890'},
    '3234567890': {'Name': '2Mathew McConaughey', 'Email': '2crungus@gmail.com', 'Phone': '3234567890'},
    '4234567890': {'Name': '3Mathew McConaughey', 'Email': '3crungus@gmail.com', 'Phone': '4234567890'},
}


#--------------------------------------------------------

def contact_add():
    while True:
        try:
            iden_choice = int(input("Would you like to use a: \n1. Phone number\nor\n2. Email Address\nas your contact identifier? Please select a number. "))
        except ValueError:
            print("Please enter a valid selection. \n")
        else:
            break

    if iden_choice == 1:
        while True:
            try:
                identifier = int(input("What is the phone number you are entering contact information for? "))
                if identifier > 1000000000:
                    pass
                else:
                    print("You chose to enter a phone number. Please enter a valid phone number (Without hyphens, including area code). ")
            except ValueError:
                print("Please enter a valid phone number. ")
            else:
                break


        name = input("What is the name of this contact? ")
        phone = identifier
        email = input("What is their email address? ")


    if iden_choice == 2:        # Potentially add in a search for an @ sign or a .com to make sure it is a valid address
        while True:
            try:
                identifier = input("What is the email address you are entering contact information for? ")
                if identifier.isSpace():
                    print("Please enter a valid non-empty email.")
            except:
                print("Please enter a valid email. ")
            else:
                break


        name = input("What is the name of this contact? ")
        email = identifier
        while True:
            try:
                phone = int(input("What is their phone number? "))
                if phone > 1000000000:
                    pass
            except ValueError:
                print("Please enter a valid phone number. ")

            else:
                break

    contacts[identifier] = {"Name" : name, "Email" : email, "Phone" : phone}

#--------------------------------------------------------

def contact_display():
    print("\nYour contacts: ")
    for contact, info in contacts.items():
        print(f'Identifier (Phone or Email): {contact} Name: {info['Name']} Email: {info['Email']} Phone #:  {info['Phone']}\n')

#--------------------------------------------------------

def contact_search():
    print("Please enter the identifier of the contact you're searching for. ")
    search_term = input("This would be a phone number or email address. ")

    for contact, info in contacts.items():
        if search_term in contact:
            print("Found! ")
            print("The contact that was found: ")
            print(f'Identifier (Phone or Email): {contact} Name: {info['Name']} Email: {info['Email']} Phone #: {info['Phone']}\n')

#--------------------------------------------------------

def contact_export():
    print("Exporting contacts...")
    with open('contacts_exported.txt', 'w') as file:
        if file:
            ovchoice = input("There is already an exported contacts file. Would you like to overwrite it? Y or N ").upper()

            if ovchoice == 'Y' or not ovchoice:
                for contact, info in contacts.items():
                    file.write(f'Identifier (Phone or Email): {contact} Name: {info['Name']} Email: {info['Email']} Phone #: {info['Phone']}\n')
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

    print('Menu: \n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Import contacts from a text file\n8. Quit')
    try:
         user_choice = int(input("\nWhat would you like to do? Please enter the number of your selection.  "))
    except ValueError:
        print("Please enter a valid number.\n")

    if user_choice == 1:
        print("You have chosen to add a new contact. ")
        contact_add()

    if user_choice == 3:
        print("You have chosen to delete a contact. ")

    if user_choice == 4:
        print("You have chosen to search for a contact. ")
        contact_search()

    if user_choice == 5:
        print("You have chosen to view your contacts. ")
        contact_display()

    if user_choice == 6:
        print("You have chosen to export your contacts to a text file. ")
        contact_export()

    if user_choice == 7:
        print("You have chosen to import contacts from a text file. ")
        contact_import()

    if user_choice == 8:
        print("Thank you for using the Contact Management System.\n ")
        break