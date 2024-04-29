
# Contact Manager

import re
contacts = {
    '1234567890': {'Name': 'Mathew McConaughey', 'Email': 'crungus@gmail.com', 'Phone': '1234567890'},
    '2234567890': {'Name': '1Mathew McConaughey', 'Email': '1crungus@gmail.com', 'Phone': '2234567890'},
    '3234567890': {'Name': '2Mathew McConaughey', 'Email': '2crungus@gmail.com', 'Phone': '3234567890'},
    '4234567890': {'Name': '3Mathew McConaughey', 'Email': '3crungus@gmail.com', 'Phone': '4234567890'},
}


#--------------------------------------------------------
# Function to add a contact
def contact_add():
    duplicate = False           # Initiate a bool for finding a duplicate and not allowing one to be added

    # Adding phone number ---------------
    while True:
        try:
            while True:
                identifier = input("What is the phone number you are entering contact information for? This will serve as an identifier: ")
                if len(identifier) == 10:                   # Make sure phone number is at least ten digits
                    break
                else:
                    print("Please enter a valid 10-digit phone number (Without hyphens, including area code). ")
        except ValueError:
            print("Please enter a valid phone number. ")    # Error handling incorrect input. From time when input was an int, but still making sure...
        else:
            break

            # Make sure duplicate phone numbers can't be used. Would interfere with searching.
    for contact, info in contacts.items():
        if identifier in info['Phone']:
            print("You cannot enter a duplicate contact. ")
            return
        
    # Adding name ---------------
    while True:
        name = input("What is the name of this contact? ")                              # Ask for name
        name_match = re.match(r"([A-Z][A-Za-z]+ [A-Za-z-]+)", name)                     # Make sure name is in valid F-L format
        if not name_match:
            print("Invalid name. Please enter a valid name (First and Last name.)")     # If name isn't in valid format
        else:
            break

    phone = identifier                                     # Set phone number to be the previously implemented identifier, since said identifier is the phone number

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'                   # Set up regex pattern to check for a valid email


    # Adding email address ---------------
    while True:
        duplicate = False
        invalid = False
        email = input("What is their email address? ").lower()  # Convert email entered to lowercase
        if not (re.match(pattern, email)):
            print("Please enter a valid email. ")               # Reject if not in @ .com format
            invalid = True
        else:
            for contact, info in contacts.items():
                if email in info['Email']:
                    print("You cannot enter a duplicate contact. ")
                    duplicate = True

        if not duplicate and not invalid:                       # Finally add contact if it is not invalid and not a duplicate vvv
            break

    contacts[identifier] = {"Name" : name, "Email" : email, "Phone" : phone}

    print(f"The following contact has been added: {contacts[identifier]}\n")

#--------------------------------------------------------
# Function to delete a contact
def contact_delete():
    while True:
        con_to_delete = input("Which contact do you want to delete? Enter its identifier. ")    # Prompt for search of phone identifier of contact to delete
        found = False                                                                           # Flag to track if the contact is found
        for contact, info in contacts.items():
            if con_to_delete in contact:
                found = True
                print("This is the contact you are deleting: ")                                 # Show user the contact they're about to delete
                print(f'Identifier: {contact} Name: {info["Name"]} Email: {info["Email"]} Phone #: {info["Phone"]}\n')
                del_choice = input("Are you sure you want to delete? Y or N. ").upper()         # Make sure user wants to delete it
                if del_choice == 'Y':
                    del contacts[con_to_delete]                                                 # Delete the contact with the specified identifier
                    print("Contact deleted successfully. ")
                    break                                                                       # Break out of the loop after deletion
                elif del_choice == 'N':
                    print("Returning to menu. \n")
                    break
        if not found:                                                                           # Was the contact asked for not in the list?
            print("That contact is not in your contacts.")
        else:
            break

#--------------------------------------------------------
# Function to display all contacts
def contact_display():
    print("\nYour contacts: ")
    for contact, info in contacts.items():          # Loop through contacts and display them in formatted form
        print(f'Identifier: {contact} Name: {info['Name']} Email: {info['Email']} Phone #:  {info['Phone']}\n')

#--------------------------------------------------------
# Function to edit part of a contact
def contact_edit():
    search_term = input("Which contact do you want to edit? Please enter its identifier. ")         # Prompts for the phone that identifies the contact

    for contact, info in contacts.items():
        if search_term in contact:                                                                  # Searches for contact that user wanted and shows it for clarity
            print("This is the contact you are editing: ")
            print(f'Identifier: {contact} Name: {info['Name']} Email: {info['Email']} Phone #: {info['Phone']}\n')

    edit_choice = input("What part of the contact would you like to edit? Name, Email or Phone? ").lower()      # Ask for part the user wants to edit and converts to lowercase
    if edit_choice == 'name':
        while True:
            new_value = input("Please enter the new name: ")
            name_match = re.match(r"([A-Z][A-Za-z]+ [A-Za-z-]+)", new_value)                                    # Making sure that the name entered is valid in F-L format with regex
            if not name_match:
                print("Invalid name. Please enter a valid name (First and Last name.)")
            else:
                break
        contacts[search_term]['Name'] = new_value                   # Updates the name in the contacts and shows it to the user
        print(f"Name updated to {new_value}.\n")



    if edit_choice == 'email':
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'                                   # Set up regex pattern for valid email
        while True:
            new_value = input("Please enter the new email: ")
            if re.match(pattern, new_value):                                    # Making sure that the email entered is valid with regex
                contacts[search_term]['Email'] = new_value                      # Update the email part of selected contact with new value
                print(f"Email updated to {new_value}.\n")
                break
            else:
                print("Please enter a valid email. ")

    if edit_choice == 'phone':
        while True:
            try:
                new_value = int(input("Please enter the new phone number: "))
                if new_value > 1000000000:                                      # Make sure added phone number is ten digits
                    break
                else:
                    print("Please enter a valid phone number.")
            except ValueError:                                                  # Error handling for non-ints
                print("Please enter a valid phone number.")
            else:
                break

        contacts[new_value] = contacts.pop(search_term)                         # Remove previous identifier and replace with new phone number (since identifiers are phone numbers)
        contacts[new_value]['Phone'] = new_value                                # Update other phone segment of contact
        print(f"Phone # updated to {new_value}.\n")

#--------------------------------------------------------
# Function to search for a contact
def contact_search():
    print("Please enter the identifier of the contact you're searching for. ")      # Asks user for their phone number they used to set the contact up
    search_term = input("This would be a phone number. ")                           # Second line is input mostly for formatting purposes (makes it look nicer)

    for contact, info in contacts.items():
        if search_term in contact:                  # Checks that the term the user wanted is present in the current contact being checked
            print("Found! ")
            print("The contact that was found: ")
            print(f'Identifier (Phone): {contact} Name: {info['Name']} Email: {info['Email']} Phone #: {info['Phone']}\n')  # Show what was found

#--------------------------------------------------------
# Function to export contacts to a text file
def contact_export():
    print("Exporting contacts...")                      
    with open('contacts_exported.txt', 'w') as file:            # Open the file for editing, if it doesn't exist, create it
        if file:                                                # If file does exist
            ovchoice = input("There is already an exported contacts file. Would you like to overwrite it? Y or N ").upper()     # If file exists, warn about overwriting it

            if ovchoice == 'Y' or not ovchoice:
                for contact, info in contacts.items():          # For each line of the contacts we have, write them to file
                    file.write(f'Identifier: {contact} Name: {info['Name']} Email: {info['Email']} Phone #: {info['Phone']}\n')
                print("Successfully exported contacts to 'exported_contacts.txt'.")
            else:
                ("Returning to menu. \n")
            
    file.close()        # Remember to close the file!

#--------------------------------------------------------
# Function to import contacts from a text file
def contact_import():

    contacts.clear()    # User has by now already specified they want to overwrite their contacts, so clear them.
    dupe = False        # Reset dupe flag to false if function resets back to start due to invalid input or a dupe being found
    while True:
        try:
            file_to_open = input("What is the name of the file you are importing contacts from? ")
            with open(file_to_open, 'r') as file:           # Open the file that the user wanted if it exists.
                for line in file:
                    dupe = False
                    info_strip = line.strip().split(' ')        # Split by whitespace
                    phone_strip = info_strip[1]                 # Put the information split into the right categories
                    name = info_strip[3]+" " + info_strip[4]
                    email_strip = info_strip[6]
                    for contact, infor in contacts.items():     # Check for duplicate phone or email - not name, people can have the same names
                        if phone_strip in infor['Phone']:
                            print("Contact detected as duplicate and skipped. ")
                            dupe = True
                    for contact, infor in contacts.items():
                        if email_strip in infor['Phone']:
                            print("Contact detected as duplicate and skipped. ")
                            dupe = True
                            return
                    if dupe == False:                           # IF no issues found, that flag is false, and so we can add the contact to the list
                        contacts[phone_strip] = {'Name': name, 'Email': email_strip, 'Phone': phone_strip}  # Add contact to dictionary
                    
        except FileNotFoundError:
            print("That file does not exist! ")
            
        else:
            break

    print("Contacts imported successfully. \n")
    file.close()        # Remember to close the file!

#--------------------------------------------------------
## MAIN CODE ##
user_choice = 0

print("Welcome to the Contact Management System!")
while True:

    # Printing menu each time we return after a function or invalid input so it isn't buried
    print('\nMenu: \n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Import contacts from a text file\n8. Quit')
    try:
         user_choice = int(input("\nWhat would you like to do? Please enter the number of your selection.  "))
    except ValueError:
        print("Please enter a valid choice.\n")     # Handle invalid overflows or characters entered instead of ints

    # User choices (1-8) - States called function to user and then will execute it
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
            contact_delete()

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
        if contacts:
            importch = input("There are already contacts in your list. This will overwrite them. Proceed? Y or N. ").upper()
            if importch == 'Y':
                contact_import()
        else:
            contact_import()

    if user_choice == 8:
        print("Thank you for using the Contact Management System.\n ")
        break

    else:
        print("Please enter a valid choice. ")