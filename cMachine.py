from cMachineClass import Coffee
from cMachineClass import Customer
from cMachineClass import Operator
import file_handler

cx = "yes"
while cx == "yes":
    c1 = Coffee("Black", 125, "Africa", 13.25)
    c2 = Coffee("Latte", 200, "Africa", 17.5)
    c3 = Coffee("Cappuccino", 300, "Spain", 10.0)
    c4 = Coffee("Espresso", 150, "America", 5.1)
    c5 = Coffee("Flat white", 250, "Spain", 5.0)
    # New Objects instantiate
    c6 = Coffee("NesCaffee", 100, "Sri lanka", 10.0)

    def display_menu_():
        f_read = open("coffee_Menu.txt", "r")
        list_of_lines = f_read.readlines()
        f_read.close()

        for line in list_of_lines:
            print(line)

    try:
        person_check = int(input("-------------------------------------***\\WELCOME DEELAKA's Coffee Service/***--------------------------------------------\nIf you're a customer enter no 1 else an operator enter no 2 :  "))
    except ValueError:
        person_check = int(input("You entered invalid value!\n===\\:-(You have only this times to enter a valid value/===\nIf you're a customer enter no 1 else an operator enter no 2 :  "))

    if person_check == 1:
        # Objects instantiate
        cus1 = Customer()
        print(cus1.ordering())

        display_menu_()
        try:
            f = int(input("Enter your coffee type no: "))
        except ValueError:
            f = int(input("You entered invalid value!\n===\\:-(You have only this times to enter a valid value/===\nEnter your coffee type no: "))

        print("***|(({Take the receipt after the Coffee brewing, then give it to the operator}))|***")

        if f == 1:
            c1 = Coffee("Black", 125, "Africa", 13.25)
            print(c1.availability_check())
            c1.order()
            print(c1.print_receipt(10))

        elif f == 2:
            c2 = Coffee("Latte", 200, "Africa", 17.5)
            print(c2.availability_check())
            c1.order()
            print(c2.print_receipt(10))

        elif f == 3:
            c3 = Coffee("Cappuccino", 300, "Spain", 10.0)
            print(c3.availability_check())
            c3.order()
            print(c3.print_receipt(10))

        elif f == 4:
            c4 = Coffee("Espresso", 150, "America", 5.1)
            print(c4.availability_check())
            c4.order()
            print(c4.print_receipt(10))

        elif f == 5:
            c5 = Coffee("Flat white", 250, "Spain", 5.0)
            print(c5.availability_check())
            c5.order()
            print(c5.print_receipt(10))

# Input new objects
        elif f == 6:
            c6 = Coffee("NesCaffee", 100, "Sri lanka", 10.0)
            print(c6.availability_check())
            c6.order()
            print(c6.print_receipt(10))

    elif person_check == 2:
        # Objects instantiate
        o1 = Operator()
        print(o1.handle())

        try:
            add_raw = input("Do you want ADD raw materials?(yes/no): ")
        except ValueError:
            add_raw = input("You entered invalid value!\n===\\:-(You have only this times to enter a valid value/===\nDo you want ADD raw materials?(yes/no): ")

        if add_raw == "yes":
            print("\n+++Choose the number of the coffee type that you want to add raw materials+++\n")
            display_menu_()

            try:
                f = int(input("Enter your coffee type no: "))
            except ValueError:
                f = int(input("You entered invalid value!\n===\\:-(You have only this times to enter a valid value/===\nEnter your coffee type no: "))

            if f == 1:
                c1 = Coffee("Black", 125, "Africa", 13.25)
                print(c1.availability_check())
                print(c1.input_raw_materials())

            elif f == 2:
                c2 = Coffee("Latte", 200, "Africa", 17.5)
                print(c2.availability_check())
                print(c2.input_raw_materials())

            elif f == 3:
                c3 = Coffee("Cappuccino", 300, "Spain", 10.0)
                print(c3.availability_check())
                print(c3.input_raw_materials())

            elif f == 4:
                c4 = Coffee("Espresso", 150, "America", 5.1)
                print(c4.availability_check())
                print(c4.input_raw_materials())

            elif f == 5:
                c5 = Coffee("Flat white", 250, "Spain", 5.0)
                print(c5.availability_check())
                print(c5.input_raw_materials())
# Insert new Objects1
            elif f == 6:
                c6 = Coffee("NesCaffee", 100, "Sri lanka", 10.0)
                print(c6.availability_check())
                print(c6.input_raw_materials())

        elif add_raw == "no":
            pass

        try:
            update = input("Do you want to enter UPDATE settings?(yes/no): ")
        except ValueError:
            update = input("You entered invalid value!\n===\\:-(You have only this times to enter a valid value/===\nDo you want to enter UPDATE settings?(yes/no): ")

        if update == "yes":
            print("+++Choose the number of the coffee type that you want to update+++\n")
            display_menu_()

            try:
                f = int(input("Enter your coffee type no: "))
            except ValueError:
                f = int(input("You entered invalid value!\n===\\:-(You have only this times to enter a valid value/===\nEnter your coffee type no: "))

            if f == 1:
                c1 = Coffee("Black", 125, "Africa", 13.25)
                print(c1.update())

            elif f == 2:
                c2 = Coffee("Latte", 200, "Africa", 17.5)
                print(c2.update())

            elif f == 3:
                c3 = Coffee("Cappuccino", 300, "Spain", 10.0)
                print(c3.update())

            elif f == 4:
                c4 = Coffee("Espresso", 150, "America", 5.1)
                print(c4.update())

            elif f == 5:
                c5 = Coffee("Flat white", 250, "Spain", 5.0)
                print(c5.update())
# Insert new Objects2
            elif f == 6:
                c6 = Coffee("NesCaffee", 100, "Sri lanka", 10.0)
                print(c6.update())

        elif update == "no":
            pass
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        try:
            dec = input("Do you want to ADD a coffee type?(yes/no)")
        except ValueError:
            dec = input("You entered invalid value!\n===\\:-(You have only this times to enter a valid value/===\nDo you want to ADD a coffee type?(yes/no)")

        if dec == "yes":
            file_handler.add_coffee_module()
            print("To activate this Coffee type, you must restart the machine!\n|||Thank you!|||\n***Coffee type was successfully added!***\n")
        elif dec == "no":
            pass
        try:
            del_coffee = input("Do you want to DELETE a coffee type?(yes/no)")
        except ValueError:
            del_coffee = input("You entered invalid value!\n===\\:-(You have only this times to enter a valid value/===\nDo you want to DELETE a coffee type?(yes/no)")

        if del_coffee == "yes":
            display_menu_()
            file_handler.del_coffee_module()
            print("To delete this Coffee type, you must restart the machine!\n|||Thank you!|||\n***Coffee type was successfully deleted!***\n")
        elif del_coffee == "no":
            pass
    try:
        cx = input("Do you want to proceed this process again?(yes/no)")
    except ValueError:
        cx = input("You entered invalid value!\n===\\:-(You have only this times to enter a valid value/===\nDo you want to proceed this process again?(yes/no)")
# ----------------------------------------------------------------------------------------------------------------------
