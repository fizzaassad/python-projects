contacts = {}
# empty dictionary called contacts to store information about contacts
def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")

    contacts[name] = {"Phone": phone, "Email": email}
    print(f"{name} added to the contact list.")

def display_contacts():
    if not contacts:
        print("Contact list is empty.")
    else:
        print("\nContacts:")
        for name, info in contacts.items():
            print(f"Name: {name}\n  Phone: {info['Phone']}\n  Email: {info['Email']}\n")
def delete_contact():
  name_to_delete = input("Enter the name of the contact to delete: ")
  if name_to_delete in contacts:
      del contacts[name_to_delete]
      print(f"{name_to_delete} deleted from the contact list.")
  else:
      print(f"{name_to_delete} not found in the contact list.")
def edit_contact():
  name_to_edit = input("Enter the name of the contact to edit: ")
  if name_to_edit in contacts:
      new_phone = input("Enter the new phone number: ")
      new_email = input("Enter the new email address: ")
      contacts[name_to_edit]["Phone"] = new_phone
      contacts[name_to_edit]["Email"] = new_email
      print(f"{name_to_edit}'s contact information updated.")
  else:
      print(f"{name_to_edit} not found in the contact list.")

def main():
    print("\n-----Contact Manager-----")
    names=input("Enter your name : ")
    print(f"\n----Welcome {names} to the Contact Manager----")
    print("Here is the list of options you can choose from:")
    while True:
        print("\n1. Add a contact")
        print("2. Display all contacts")
        print("3. Delete a contact")
        print("4. Edit a contact")
        print("5.exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            display_contacts()
        elif choice == "3":
           delete_contact()
        elif choice == "4":
          edit_contact()
        elif choice == "5":
            print("Exiting the contact list program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
