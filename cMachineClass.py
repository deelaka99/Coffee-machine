import time


class Person:
    def __init__(self):
        self.name = "Someone"

    def handle(self):
        return '{} is handling the coffee machine'.format(self.name)
# ----------------------------------------------------------------------------------------------------------------------


class Customer(Person):
    def ordering(self):
        return '***{} is going to order***\n'.format(self.name)
# ----------------------------------------------------------------------------------------------------------------------


class Operator(Person):
    def handle(self):  # overriding the handle method
        self.name = input("Enter your name(operator):")
        return '***\\;-) {} is handling the coffee machine/***\n'.format(self.name)
# ----------------------------------------------------------------------------------------------------------------------


class Coffee:
    def __init__(self, c_type, price, country_origin, avail_lvl_raw):
        self.c_type = c_type
        self.price = price
        self.country_origin = country_origin
        self.avail_lvl_raw = avail_lvl_raw  # check using kilo gram
        self.__pay_statues = None
        self.pay_statues = ""
        self.amount = 0  # coffees could be brewed at a one time from 1 kg is 20

    def get_pay_statues(self):
        return self.__pay_statues

    def print_receipt(self, discount):
        # Python time.strftime()
        named_tuple = time.localtime()  # get struct_time
        time_string = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)

        c_type = self.c_type
        price = self.price
        amount = self.amount
        if self.amount > 8:
            f1 = open("receipt.txt", "a")
            f1.write(str("-------------------------------------***\\DEELAKA's Coffee Service/***--------------------------------------------\nCoffee type :" + c_type + "\nAmount :" + str(amount) + "\nTotal price : LKR." + str(price) + "X" + str(amount) + " - LKR." + str(price * amount * discount / 100) + "= LKR." + str(price * amount - price * amount * discount / 100) + "\nYou got a " + str(discount) + "% discount\n" + time_string + "\n-------------------------------------***\\Thank you!Come again/***------------------------------------------------\n\n"))
            f1.close()
            return "You got a discount " + str(discount) + "% from  your total price\nYour new total payment is LKR." + str(price * amount - price * amount * discount / 100) + "\nYour change is LKR." + str(price * amount * discount / 100) + "\nGet your change from operator!"
        else:
            f1 = open("receipt.txt", "a")
            f1.write(str("-------------------------------------***\\DEELAKA's Coffee Service/***--------------------------------------------\nCoffee type :" + c_type + "\nAmount :" + str(amount) + "\nTotal price : LKR." + str(price) + "X" + str(amount) + "= LKR." + str(price * amount) + "\n" + time_string + "\n-------------------------------------***\\Thank you!Come again/***------------------------------------------------\n\n"))
            f1.close()
        return "\nTake your receipt!"

    def order(self):
        c_type = self.c_type
        price = self.price
        country = self.country_origin
        raw = self.avail_lvl_raw
        try:
            obj_no = input("Enter the coffee type no again: ")
        except ValueError:
            obj_no = input("You entered invalid value!\n===\\:-(You have only this times to enter a valid value/===\nEnter the coffee type no again: ")
        try:
            self.amount = int(input("Enter amount of the cups : "))
        except ValueError:
            self.amount = int(input("You entered invalid value!\n===\\:-(You have only this times to enter a valid value/===\nEnter amount of the cups : "))
# =================================================FILE HANDLING PART of the order method===============================
        raw_check = str("    c" + obj_no + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country + "\", " + str(raw) + ")")
        raw_add = str("    c" + obj_no + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country + "\", " + str(raw - self.amount*(1/20)) + ")")

        fin = open("cMachine.py", "r+")
        lines = fin.readlines()
        fin.seek(0)
        fin.truncate()
        for line in lines:
            if line.startswith(raw_check):
                line = line.replace(raw_check, raw_add)
            fin.write(line)
        fin.close()

        raw_check = str("            c" + obj_no + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country + "\", " + str(raw) + ")")
        raw_add = str("            c" + obj_no + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country + "\", " + str(raw - self.amount*(1/20)) + ")")

        fin = open("cMachine.py", "r+")
        lines = fin.readlines()
        fin.seek(0)
        fin.truncate()
        for line in lines:
            if line.startswith(raw_check):
                line = line.replace(raw_check, raw_add)
            fin.write(line)
        fin.close()

        raw_check = str("                c" + obj_no + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country + "\", " + str(raw) + ")")
        raw_add = str("                c" + obj_no + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country + "\", " + str(raw - self.amount*(1/20)) + ")")

        fin = open("cMachine.py", "r+")
        lines = fin.readlines()
        fin.seek(0)
        fin.truncate()
        for line in lines:
            if line.startswith(raw_check):
                line = line.replace(raw_check, raw_add)
            fin.write(line)
        fin.close()

        raw_check = "{" + str(obj_no) + "}." + c_type + " Coffee        *{Price--------LKR." + str(price) + "}        *{Origin--------" + country + "}        *{Available raw--------" + str(raw) + "Kg}"
        raw_add = "{" + str(obj_no) + "}." + c_type + " Coffee        *{Price--------LKR." + str(price) + "}        *{Origin--------" + country + "}        *{Available raw--------" + str(raw - self.amount*(1/20)) + "Kg}"

        fin = open("coffee_Menu.txt", "r+")
        lines = fin.readlines()
        fin.seek(0)
        fin.truncate()
        for line in lines:
            if line.startswith(raw_check):
                line = line.replace(raw_check, raw_add)
            fin.write(line)
        fin.close()

        if self.amount == 1:
            print("One ", c_type, " coffee has been ordered\n*** Total price is LKR.", str(price), ".***\n")

        else:
            print(str(self.amount), " ", c_type, " coffees have been ordered\n*** Total price is LKR.", str(price*self.amount), ".***\n")
# ======================================================================================================================
        print(self.availability_check())
        if self.avail_lvl_raw == 0:
            pass
        else:
            print(self.money_inserting())
            print(self.brew())
# ======================================================================================================================

    def input_raw_materials(self):
        print("\n**++--WELCOME to ADD RAW MATERIALS Settings:--++**\n**++--You're going to add ", self.c_type, " coffee's raw material--++**\n")
        c_type = self.c_type
        price = self.price
        country = self.country_origin
        raw = self.avail_lvl_raw
        try:
            obj_no = input("Enter the coffee type no again: ")
        except ValueError:
            obj_no = input("You entered invalid value!\n===\\:-(You have only this times to enter a valid value/===\nEnter the coffee type no again: ")

        try:
            x = float(input("Enter your raw_material amount(Kg):"))
        except ValueError:
            x = float(input("You entered invalid value!\n===\\:-(You have only this times to enter a valid value/===\nEnter your raw_material amount(Kg):"))
# ===========================FILE HANDLING PART of the input_raw materials method=======================================
        raw_check = str("    c" + obj_no + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country + "\", " + str(raw) + ")")
        raw_add = str("    c" + obj_no + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country + "\", " + str(raw + x) + ")")

        fin = open("cMachine.py", "r+")
        lines = fin.readlines()
        fin.seek(0)
        fin.truncate()
        for line in lines:
            if line.startswith(raw_check):
                line = line.replace(raw_check, raw_add)
            fin.write(line)
        fin.close()

        raw_check = str("            c" + obj_no + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country + "\", " + str(raw) + ")")
        raw_add = str("            c" + obj_no + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country + "\", " + str(raw + x) + ")")

        fin = open("cMachine.py", "r+")
        lines = fin.readlines()
        fin.seek(0)
        fin.truncate()
        for line in lines:
            if line.startswith(raw_check):
                line = line.replace(raw_check, raw_add)
            fin.write(line)
        fin.close()

        raw_check = str("                c" + obj_no + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country + "\", " + str(raw) + ")")
        raw_add = str("                c" + obj_no + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country + "\", " + str(raw + x) + ")")

        fin = open("cMachine.py", "r+")
        lines = fin.readlines()
        fin.seek(0)
        fin.truncate()
        for line in lines:
            if line.startswith(raw_check):
                line = line.replace(raw_check, raw_add)
            fin.write(line)
        fin.close()

        raw_check = "{" + str(obj_no) + "}." + c_type + " Coffee        *{Price--------LKR." + str(price) + "}        *{Origin--------" + country + "}        *{Available raw--------" + str(raw) + "Kg}"
        raw_add = "{" + str(obj_no) + "}." + c_type + " Coffee        *{Price--------LKR." + str(price) + "}        *{Origin--------" + country + "}        *{Available raw--------" + str(raw + x) + "Kg}"

        fin = open("coffee_Menu.txt", "r+")
        lines = fin.readlines()
        fin.seek(0)
        fin.truncate()
        for line in lines:
            if line.startswith(raw_check):
                line = line.replace(raw_check, raw_add)
            fin.write(line)
        fin.close()
        return str("Your entered " + str(x) + "Kg of " + c_type + " raw material! \n Full amount of the " + c_type + " raw material is " + str(raw + x) + "Kg.\nTo activate this Coffee type, you must restart the machine!\n|||Thank you!|||\n***Raw materials were successfully added!***\n")
# ======================================================================================================================

    def availability_check(self):
        alr = self.avail_lvl_raw - self.amount*(1/20)
        if alr == 0:
            return str("***Oh sorry!***\nRaw materials are ended of " + self.c_type + " Coffee. Please contact an operator...\nInput Raw materials!\n")
        elif alr < 2:
            return str("***Attention:-***\nRaw materials are lesser than 2Kg!\nYou can brew " + str(int(self.avail_lvl_raw * 20-self.amount)) + " of " + self.c_type + " coffee cups\n")

        else:
            return str("***Be cool!***\n+++Present value of raw materials: " + str(alr) + "Kg +++\nYou can brew/order " + str(int(self.avail_lvl_raw * 20-self.amount)) + " of " + self.c_type + " coffee cups!\n")

    def money_inserting(self):
        try:
            money_paid = int(input("Enter your money here :LKR."))
        except ValueError:
            money_paid = int(input("You entered invalid value!\n===\\:-(You have only this times to enter a valid value/===\nEnter your money here :LKR."))

        self.pay_statues = self.get_pay_statues()
        if money_paid == self.amount*self.price:
            self.pay_statues = "Good"
            return str("**\\Please wait few seconds/**\n++your coffee is being made++\n***\\Thank you!/***\n")
        elif money_paid < self.amount*self.price:
            self.pay_statues = "Bad"
            return str("---Your money isn't match with price---\n+++You must input more LKR." + str(self.amount*self.price-money_paid) + " for your item/s.+++\n")
        else:
            self.pay_statues = "Bad"
            return str("---Your entered too than LKR." + str(self.amount*self.price))

    def brew(self):
        if self.get_pay_statues() == "Good":
            if self.amount > 1:
                return str(":-) Your " + str(self.amount) + " " + self.c_type + " coffees are being brewed\n")

            else:
                return str(";-) Your  coffee is being brewed\n")
        elif self.get_pay_statues() == "Bad":
            return str(";-) Can't brew now\n Please try again!\n")

    def update(self):
        print("\n**++--WELCOME to UPDATE Settings:--++**\n**++--You're going to modify ", self.c_type, " coffee's module!--++**\n")
        earlier_c_type = self.c_type
        earlier_price = self.price
        earlier_country = self.country_origin
        earlier_raw = self.avail_lvl_raw

        try:
            obj_no = input("Enter the coffee type no: ")
        except ValueError:
            obj_no = input("You entered invalid value!\n===\\:-(You have only this times to enter a valid value/===\nEnter the coffee type no: ")

        try:
            new_c_type = input("Enter the coffee type: ")
        except ValueError:
            new_c_type = input("You entered invalid value!\n===\\:-(You have only this times to enter a valid value/===\nEnter the coffee type: ")

        try:
            new_avail_lvl_raw = int(input("Enter the raw materials:"))
        except ValueError:
            new_avail_lvl_raw = int(input("You entered invalid value!\n===\\:-(You have only this times to enter a valid value/===\nEnter the raw materials:"))

        try:
            new_price = int(input("Enter the price: LKR"))
        except ValueError:
            new_price = int(input("You entered invalid value!\n===\\:-(You have only this times to enter a valid value/===\nEnter the price: LKR"))

        try:
            new_country_origin = input("Enter the coffee origin: ")
        except ValueError:
            new_country_origin = input("You entered invalid value!\n===\\:-(You have only this times to enter a valid value/===\nEnter the coffee origin country: ")

# =================================FILE HANDLING PART of the update method==============================================
        modify_check = str("    c" + obj_no + " = Coffee(\"" + earlier_c_type + "\", " + str(earlier_price) + ", \"" + earlier_country+ "\", " + str(earlier_raw) + ")")
        modify_add = str("    c" + obj_no + " = Coffee(\"" + new_c_type + "\", " + str(new_price) + ", \"" + new_country_origin+ "\", " + str(new_avail_lvl_raw) + ")")

        fin = open("cMachine.py", "r+")
        lines = fin.readlines()
        fin.seek(0)
        fin.truncate()
        for line in lines:
            if line.startswith(modify_check):
                line = line.replace(modify_check, modify_add)
            fin.write(line)
        fin.close()

        modify_check = str("            c" + obj_no + " = Coffee(\"" + earlier_c_type + "\", " + str(earlier_price) + ", \"" + earlier_country+ "\", " + str(earlier_raw) + ")")
        modify_add = str("            c" + obj_no + " = Coffee(\"" + new_c_type + "\", " + str(new_price) + ", \"" + new_country_origin+ "\", " + str(new_avail_lvl_raw) + ")")

        fin = open("cMachine.py", "r+")
        lines = fin.readlines()
        fin.seek(0)
        fin.truncate()
        for line in lines:
            if line.startswith(modify_check):
                line = line.replace(modify_check, modify_add)
            fin.write(line)
        fin.close()

        modify_check = str("                c" + obj_no + " = Coffee(\"" + earlier_c_type + "\", " + str(earlier_price) + ", \"" + earlier_country+ "\", " + str(earlier_raw) + ")")
        modify_add = str("                c" + obj_no + " = Coffee(\"" + new_c_type + "\", " + str(new_price) + ", \"" + new_country_origin+ "\", " + str(new_avail_lvl_raw) + ")")

        fin = open("cMachine.py", "r+")
        lines = fin.readlines()
        fin.seek(0)
        fin.truncate()
        for line in lines:
            if line.startswith(modify_check):
                line = line.replace(modify_check, modify_add)
            fin.write(line)
        fin.close()

        modify_check = "{" + str(obj_no) + "}." + earlier_c_type + " Coffee        *{Price--------LKR." + str(earlier_price) + "}        *{Origin--------" + earlier_country + "}        *{Available raw--------" + str(earlier_raw) + "Kg}"
        modify_add = "{" + str(obj_no) + "}." + new_c_type + " Coffee        *{Price--------LKR." + str(new_price) + "}        *{Origin--------" + new_country_origin + "}        *{Available raw--------" + str(new_avail_lvl_raw) + "Kg}"
        fin = open("coffee_Menu.txt", "r+")
        lines = fin.readlines()
        fin.seek(0)
        fin.truncate()
        for line in lines:
            if line.startswith(modify_check):
                line = line.replace(modify_check, modify_add)
            fin.write(line)
        fin.close()
        return "To activate this Coffee type, you must restart the machine!\n|||Thank you!|||\n***Coffee type was successfully modified!***\n"
# --------------End line of the area of class's ------------------------------------------------------------------------
