'''
AUTHOR: ServerLite
DATE: 11/29/24
'''

### CONTACT BOOK CLASS ###
class ContactBook:
    def __init__(self):
        self.__book = list()

    # Gets and edits the first name of the book
    def __getFirstLastName(self, name):
        name = name.split(" ",1)
        first_name = None
        last_name = None

        if len(name) == 1:
            first_name = name[0]
        else:
            first_name, last_name = name[0], name[1]

        return first_name, last_name

    # Gets and edits the number of the book
    def __getNumber(self, number):
        number = str(number)
        if len(number) > 10:
            print("Your number is too long, shrinking it down")
            number = number[0:10]
        elif len(number) < 10:
            print("Your number is too short, adding zero's at the end")
            for i in range(10-len(number)): number += "0"
        return number

    # Adds a contact to the book
    def add(self, name:str="UnknownName", number:str=0):
        # Customizing then name
        first_name, last_name = self.__getFirstLastName(name)

        # Customizing the number
        number: str = self.__getNumber(number)

        new_contact = [first_name, last_name, number]
        self.__book.append(new_contact)

    # Edits the contact in the book
    def edit(self, name:str="UnknownName", number:str=0):
        first_name, last_name = self.__getFirstLastName(name)

        for contact in self.__book:
            if contact[0] == first_name and contact[1] == last_name:
                contact[2] = self.__getNumber(number)
                return
            
        print(f"{name} was never found in your contact book")

    # Removes the contacts from the book
    def remove(self, name="UnknownName"):
        first_name, last_name = self.__getFirstLastName(name)

        for index, contact in enumerate(self.__book):
            if contact[0] == first_name and contact[1] == last_name:
                self.__book.pop(index)
                return

        print(f"{name} was never found in your contact book")

    # Displays your entire contact book
    def view(self):
        for index, contact in enumerate(self.__book):
            first_name = contact[0]
            last_name = contact[1]
            number = contact[2]

            print(f"({index+1})")
            print(f"\tFirst Name: {first_name}")
            if last_name: print(f"\tLast Name: {last_name}")
            print(f"\tPhone Number ({number[0:3]}) {number[3:6]} - {number[6:10]}")

if __name__ == "__main__":
    # We need to make our contact book
    contact_book = ContactBook()

    # Adding contacts
    contact_book.add("John Doe", 1342093501)
    contact_book.add("Jane Doe", 1342093501)
    contact_book.add("Bob Goner", 1342093501)

    # Editing a non-existing contact: Will do nothing
    contact_book.edit("John Do", 6)

    # Removing an existing contact: Will remove that person (Bob Goner)
    contact_book.remove("Bob Goner")

    # Views the contact book
    contact_book.view()