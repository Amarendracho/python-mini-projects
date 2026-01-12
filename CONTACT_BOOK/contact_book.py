

add_contact_list = {}

def add_contact():
    global add_contact_list

    name = input("Enter Contact Name : ").strip()
    phone = input("Enter Contact Number : ").strip()

    if name == "" or phone == "":
        print("Name/Number cannot be empty ⛔️")
        return

    add_contact_list[name] = phone
    print(f"✅ Saved: {name} -> {phone}")

def view_contact():
    if not add_contact_list:
        print("📭 No contacts saved yet.")

    print("\n--- All Contacts ---")
    for name, phone in add_contact_list.items():
        print(f"{name} : {phone}")

def search_contact():
    name = input("Enter name to search : ").strip()

    if name not in add_contact_list:
        print("Contact not Saved!")
        return

    if name in add_contact_list:
        print(f"✅Found Contact {name} -> {add_contact_list[name]}")
    else:
        print("❌ Contact not found")

def delete_contact():
    name = input("Enter name to delete: ").strip()

    if name in add_contact_list:
        del add_contact_list[name]
        print(f"🗑️ Deleted contact: {name}")
    else:
        print("❌ Contact not found")


def bye():
    print("Thank you, Have a good day.👋")

def contact_book_manager():
    while True:
        userinput = input("select Menu \n"
            "1) Add Contact \n"
            "2) View Contact \n"
            "3) Search Contact \n"
            "4) Delete Contact \n"
            "5) Exit \n"
            "please choose : ").strip().lower()

        if userinput in ["1", "Add Contact", "add"]:
             add_contact()
        elif userinput in ["2", "show", "view contact", "view"]:
            view_contact()
        elif userinput in ["3","search", "Search", "find"]:
            search_contact()
        elif userinput in ["4", "delete", "Delete"]:
            delete_contact()
        elif userinput in ["5", "exit","Exit"]:
            bye()
            return
        else:
            print("Invalid input. Please try again.")


contact_book_manager()