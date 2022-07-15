TABLE = "{:<50} {:<50} {:<50} {:<50} {:<50} {:<50} {:<50} {:<50}"


class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.email = email


class Addressbook:

    def __init__(self, address_book_name):
        """
                This is constructor
                Args:
                    address_book_name: Taking addressbook name from user
                """
        self.address_book_name = address_book_name
        self.contact_dict = {}


def add_addressbook():
    """
            Adding address book name and also checking book present or not. If present then don't add
            but if not then add book.
        Returns: None
        """
    try:
        address_book_name = input("Enter Address Book Name You Want To Add: ")
        address_book = Addressbook(address_book_name)
        address_obj = address_book_dict.get(address_book_name)
        if address_obj:
            print("Book Name Already Exist")
            return
        address_book_dict.update({address_book_name: address_book})
        print("{} Added Successfully".format(address_book_name))
    except Exception as e:
        print("Please Enter Valid Book Name", e)


def display_address_book():
    """
        Displaying list of addressbook name present
        Returns: None
        """
    print("Book Name")
    for k in address_book_dict:
        print(k)


def add_contact():
    """
        Adding contact to address book but before that I'm checking contact is present or not. If not
        then add that contact otherwise don't add
        Returns: None
        """
    try:
        address_book_name = input("Enter Book Name To Add Contact: ")
        book_obj = address_book_dict.get(address_book_name)
        if not book_obj:
            print("Book Having Name {} Not Found".format(address_book_name))
            return
        first_name = input("Enter First Name: ")
        if book_obj.contact_dict.get(first_name):
            print("Contact Already Exist")
            return
        last_name = input("Enter Last Name: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip = int(input("Enter Zip_Code: "))
        phone = int(input("Enter Phone Number: "))
        email = input("Enter Email: ")
        contact = Contact(first_name, last_name, address, city, state, zip, phone, email)
        book_obj.contact_dict.update({contact.first_name: contact})
        print("Contact Added Successfully")
    except Exception as e:
        print("Please Enter Correct Book Name", e)


def display_contact():
    """
        Displaying the contacts present in particular address book
        Returns: None
        """
    try:
        address_book_name = input("Enter Book Name To Display Contact: ")
        book_obj = address_book_dict.get(address_book_name)
        if not book_obj:
            print("Book Having Name {} Not Found".format(address_book_name))
            return
        print(TABLE.format("First_Name","Last_Name","Address","City","State","Zip-Code","Phone_Number","Email_Id"))

        print()
        for k, v in book_obj.contact_dict.items():
            print(TABLE.format(v.first_name,v.last_name,v.address,v.city,v.state,v.zip,v.phone,v.email))
            print()
    except Exception as e:
        print("Please Enter Correct Book Name!")


def edit_contact():
    """
        Editing existing contact on the basis of first name
        Returns: None
        """
    try:
        address_book_name = input("Enter Book Name To Edit Contact: ")
        book_obj = address_book_dict.get(address_book_name)
        if not book_obj:
            print("No Book Found With This Name")
            return

        first_name = input("Enter Name To Edit: ")
        contact_obj = book_obj.contact_dict.get(first_name)
        if not contact_obj:
            print("No Contact Found having name {}".format(first_name))
            return
        last_name = input("Enter last name: ")
        address = input("Enter Address: ")
        city = input("Enter city: ")
        state = input("Enter state: ")
        zip = input("Enter zip code: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contact_dict = {"first_name": first_name if first_name != "" else contact_obj.first_name,
                        "last_name": last_name if last_name != "" else contact_obj.last_name,
                        "Address": address if address != "" else contact_obj.address,
                        "city": city if city != "" else contact_obj.city,
                        "state": state if state != "" else contact_obj.state,
                        "zip_code": zip if zip != "" else contact_obj.zip,
                        "phone": phone if phone != "" else contact_obj.phone,
                        "email": email if email != "" else contact_obj.email
                        }

        contact_obj.first_name = contact_dict.get("first_name")
        contact_obj.last_name = contact_dict.get("last_name")
        contact_obj.address = contact_dict.get("Address")
        contact_obj.city = contact_dict.get("city")
        contact_obj.state = contact_dict.get("state")
        contact_obj.zip = contact_dict.get("zip_code")
        contact_obj.phone = contact_dict.get("phone")
        contact_obj.email = contact_dict.get("email")
        print("Contact successfully updated")

    except Exception as e:
        print("Enter valid book name", e)


def delete_contact():
    """
       Deleting contact person using their first name and before that checking contact is present or not
       Returns: None
       """
    try:
        address_book_name = input("Enter book name to delete contact: ")
        book_obj = address_book_dict.get(address_book_name)
        if not book_obj:
            print("Book name not found")
            return
        first_name = input("Enter name to delete: ")
        book_obj.contact_dict.pop(first_name)
        print("Contact deleted successfully")
    except Exception as e:
        print("Please enter valid input", e)


if __name__ == "__main__":
    address_book_dict = {}
    while True:
        print("Choose below option to perform task")
        print("1. Add an address book\n"
              "2. Display address book\n"
              "3. Add contact\n"
              "4. Display contact\n"
              "5. Edit contact\n"
              "6. Delete contact\n"
              "0. Exit address book Program...")

        choice = {1: add_addressbook,
                  2: display_address_book,
                  3: add_contact,
                  4: display_contact,
                  5: edit_contact,
                  6: delete_contact}
        print()
        try:
            userinput = int(input("Enter Your choice: "))
            if userinput != 0:
                choice.get(userinput)()
            elif userinput == 0:
                print("Existing Address Book system !!")
                print()
        except Exception as e:
            print("Please Enter Valid Input ", e)
            print()
