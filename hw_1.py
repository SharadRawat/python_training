#!/usr/bin/env python3

import sys

class phonebook:
    def __init__(self):
        self.database = {}

    def create_new_contact(self):
        print(" *************** Creating a new contact ***********")

        print(" Type the name of the person. ")
        name = str(input())
        print(" Type the phone number. ")
        num = str(input())

        self.database.update({name: num})
        print(" Number added in the database. ")

    def find_phone_num(self):
        print(" *************** Finding a phone number ***********")

        print(" Type the name of the person. ")
        name = str(input())

        try:
            phone_num = self.database.get(name)
            print(" The number is {} ".format(phone_num))

        except KeyError:
            print(" Name not found. ")
            sys.exit(0)


    def change_phone_num(self):
        print(" *************** Changing a phone number ***********")

        print(" Type the name of the person. ")
        name = str(input())
        print(" Type the new phone number. ")
        num = input()

        try:
            self.database[name] = num

        except KeyError:
            print(" Name not found. ")
            sys.exit(0)


    def remove_contact(self):
        print(" *************** Removing a contact ***********")

        print(" Type the name of the person. ")
        name = str(input())

        try:
            self.database.pop(name)

        except KeyError:
            print(" Name not found. ")
            sys.exit(0)



    def print(self):
        print(" *************** Printing the database ***********")

        for key in self.database.keys():
            entry = " Name: {},  Phone Number: {} ".format(key, self.database.get(key))
            print(entry)


if __name__ == "__main__":

    try:
        database = phonebook()
        function_call_dict = {1 : database.create_new_contact, 2 : database.find_phone_num, 3 : database.change_phone_num , 4 : database.remove_contact, 5 : database.print}
        print(" What do you want, man/woman? \n 1) Create a new entry \n 2) Find a number \n 3) Change a phone number \n 4) Remove a contact \n 5) Print")


        while True:
            print(" \n Type a number from (1,5)    ")
            usr_response = int(input())
            _ = function_call_dict[usr_response]()

    except KeyboardInterrupt:
        print(" Keyboard Interrupt by user.")
        sys.exit(0)







