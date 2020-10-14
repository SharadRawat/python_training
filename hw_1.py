#!/usr/bin/env python3

import sys

class phonebook:
    def __init__(self):
        self.database = {}

    def create_new_contact(self):
        print(" \n *************** Creating a new contact *********** \n ")

        print(" Type the name of the person. ")
        name = str(input())
        print(" Type the phone number. ")
        num = str(input())

        self.database.update({name: num})
        print(" Number added in the database. ")

    def find_phone_num(self):
        print(" \n *************** Finding a phone number *********** \n ")

        print(" Type the name of the person. ")
        name = str(input())

        phone_num = self.database.get(name)
        print(" The number is {} ".format(phone_num))




    def change_phone_num(self):
        print(" \n *************** Changing a phone number *********** \n")

        print(" Type the name of the person. ")
        name = str(input())
        print(" Type the new phone number. ")
        num = input()

        if name in self.database:
            self.database[name] = num

        else:
            print(" Name not found.")


    def remove_contact(self):
        print(" \n *************** Removing a contact *********** \n ")

        print(" Type the name of the person. ")
        name = str(input())

        try:
            self.database.pop(name)

        except KeyError:
            print(" Name not found. ")
            pass



    def print(self):
        print(" \n *************** Printing the database *********** \n \n")

        for key in self.database.keys():
            entry = " Name: {},  Phone Number: {} ".format(key, self.database.get(key))
            print(entry)


if __name__ == "__main__":

    try:
        database = phonebook()
        function_call_dict = {1 : database.create_new_contact, 2 : database.find_phone_num, 3 : database.change_phone_num , 4 : database.remove_contact, 5 : database.print}
        print(" What do you want, man/woman? \n 1) Create a new entry \n 2) Find a number \n 3) Change a phone number \n 4) Remove a contact \n 5) Print")


        try:
            while True:
                print(" \n Type a number from (1,5)    ")
                usr_response = int(input())
                _ = function_call_dict.get(usr_response)()

        except Exception as e:
            print(e)
            print(" This input does exist. Try again.")

    except KeyboardInterrupt:
        print(" Keyboard Interrupt by user.")
        sys.exit(0)







