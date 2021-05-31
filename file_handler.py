# ----------------------LOGICAL FUNCTION-add_coffee_module--------------------------------------------------------------
def add_coffee_module():
    print("\n\t\t\t\t\tWELCOME!\n-------------------**++--You're going to Add a new Coffee module!--++**-------------------\n")
    obj_no = input("Enter Coffee type no: ")
    c_type = input("Enter Coffee type name: ")
    price = float(input("Enter the price: "))
    country_origin = input("Enter the country origin: ")
    avail_lvl_raw = float(input("Enter the amount of the raw material(Kg): "))
    #  Print after the '    # New Objects instantiate'
    o1_to_check = "    # New Objects instantiate"
    o1_to_add = str("    c" + str(obj_no) + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country_origin + "\", " + str(avail_lvl_raw) + ")")

    with open("cMachine.py", 'r+') as file_to_write:
        lines = file_to_write.readlines()
        file_to_write.seek(0)
        file_to_write.truncate()
        for line in lines:
            if line.startswith(o1_to_check):
                line = line.rstrip("\n") + "\n" + o1_to_add + "\n"
            file_to_write.write(line)
    file_to_write.close()

    #  Print after the 'Input new Objects'
    o1_to_check = "# Input new objects"
    o1_to_add = "        elif f == " + str(obj_no) + ":\n            c" + str(obj_no) + " = Coffee("'"' + c_type + '"'", " + str(price) + ", "'"' + country_origin + '"'", " + str(avail_lvl_raw) + ")\n            print(c" + str(obj_no) + ".availability_check())\n            c" + str(obj_no) + ".order()\n            print(c" + str(obj_no) + ".print_receipt(10))\n"

    with open("cMachine.py", 'r+') as file_to_write:
        lines = file_to_write.readlines()
        file_to_write.seek(0)
        file_to_write.truncate()
        for line in lines:
            if line.startswith(o1_to_check):
                line = line.rstrip("\n") + "\n" + o1_to_add + "\n"
            file_to_write.write(line)
    file_to_write.close()

    #  Print after the 'Insert new Objects1'
    o2_to_check = "# Insert new Objects1"
    o2_to_add = "            elif f == " + str(obj_no) + ":\n                c" + str(obj_no) + " = Coffee("'"' + c_type + '"'", " + str(price) + ", "'"' + country_origin + '"'", " + str(avail_lvl_raw) + ")\n                print(c" + str(obj_no) + ".availability_check())\n                print(c" + str(obj_no) + ".input_raw_materials())\n"

    with open("cMachine.py", 'r+') as file_to_write:
        lines = file_to_write.readlines()
        file_to_write.seek(0)
        file_to_write.truncate()
        for line in lines:
            if line.startswith(o2_to_check):
                line = line.rstrip("\n") + "\n" + o2_to_add + "\n"
            file_to_write.write(line)
    file_to_write.close()

    #  Print after the 'Insert new Objects2'
    o3_to_check = "# Insert new Objects2"
    o3_to_add = "            elif f == " + str(obj_no) + ":\n                c" + str(obj_no) + " = Coffee("'"' + c_type + '"'", " + str(price) + ", "'"' + country_origin + '"'", " + str(avail_lvl_raw) + ")\n                print(c" + str(obj_no) + ".update())\n"

    with open("cMachine.py", 'r+') as file_to_write:
        lines = file_to_write.readlines()
        file_to_write.seek(0)
        file_to_write.truncate()
        for line in lines:
            if line.startswith(o3_to_check):
                line = line.rstrip("\n") + "\n" + o3_to_add + "\n"
            file_to_write.write(line)
    file_to_write.close()

    f_append = open("coffee_Menu.txt", "a")
    f_append.write("\n{" + str(obj_no) + "}." + c_type + " Coffee        *{Price--------LKR." + str(price) + "}        *{Origin--------" + country_origin + "}        *{Available raw--------" + str(avail_lvl_raw) + "Kg}")
    f_append.close()

#  ---------------------------------------------------------------------------------------------------------------------


# ----------------------LOGICAL FUNCTION-del_coffee_module--------------------------------------------------------------
def del_coffee_module():
    print("\n\t\t\t\t\tWELCOME!\n-------------------**++--You're going to Delete a Coffee module!--++**-------------------\n")
    obj_no = int(input("Enter Coffee type no: "))
    c_type = input("Enter Coffee type name: ")
    price = float(input("Enter the price: "))
    country_origin = input("Enter the country origin: ")
    avail_lvl_raw = float(input("Enter the amount of the raw material(Kg): "))

    #  Delete a text
    del1_to_check = "    c" + str(obj_no) + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country_origin + "\", " + str(avail_lvl_raw) + ")"
    with open("cMachine.py", 'r+') as file_to_write:
        f = open("coffee_Menu.txt", "r")
        lines = f.readlines()
        f = open("coffee_Menu.txt", "w")
        for line in lines:
            if line.strip("\n") != del1_to_check:
                f.write(line)
        f.close()

    #  Delete a text
    if obj_no == 1:
        del2_to_check = "        if f == " + str(obj_no) + ":\n            c" + str(obj_no) + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country_origin + "\", " + str(avail_lvl_raw) + ")\n            print(c" + str(obj_no) + ".availability_check())\n            c" + str(obj_no) + ".order()\n            print(c" + str(obj_no) + ".print_receipt(10))"
        f = open("coffee_Menu.txt", "r")
        lines = f.readlines()
        f = open("coffee_Menu.txt", "w")
        for line in lines:
            if line.strip("\n") != del2_to_check:
                f.write(line)
        f.close()
    else:
        del2_to_check = "        elif f == " + str(obj_no) + ":\n            c" + str(obj_no) + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country_origin + "\", " + str(avail_lvl_raw) + ")\n            print(c" + str(obj_no) + ".availability_check())\n            c" + str(obj_no) + ".order()\n            print(c" + str(obj_no) + ".print_receipt(10))"
        f = open("coffee_Menu.txt", "r")
        lines = f.readlines()
        f = open("coffee_Menu.txt", "w")
        for line in lines:
            if line.strip("\n") != del2_to_check:
                f.write(line)
        f.close()

    #  Delete a text
    if obj_no == 1:
        del3_to_check = "            if f == " + str(obj_no) + ":\n                c" + str(obj_no) + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country_origin + "\", " + str(avail_lvl_raw) + ")\n                print(c" + str(obj_no) + ".availability_check())\n                print(c" + str(obj_no) + ".input_raw_materials())"
        f = open("coffee_Menu.txt", "r")
        lines = f.readlines()
        f = open("coffee_Menu.txt", "w")
        for line in lines:
            if line.strip("\n") != del3_to_check:
                f.write(line)
        f.close()
    else:
        del3_to_check = "            elif f == " + str(obj_no) + ":\n                c" + str(obj_no) + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country_origin + "\", " + str(avail_lvl_raw) + ")\n                print(c" + str(obj_no) + ".availability_check())\n                print(c" + str(obj_no) + ".input_raw_materials())"
        with open("cMachine.py", 'r+') as file_to_write:
            f = open("coffee_Menu.txt", "r")
            lines = f.readlines()
            f = open("coffee_Menu.txt", "w")
            for line in lines:
                if line.strip("\n") != del3_to_check:
                    f.write(line)
            f.close()

    #  Delete a text
        if obj_no == 1:
            del4_to_check = "            if f == " + str(obj_no) + ":\n                c" + str(obj_no) + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country_origin + "\", " + str(avail_lvl_raw) + ")\n                print(c" + str(obj_no) + ".update())"
            f = open("coffee_Menu.txt", "r")
            lines = f.readlines()
            f = open("coffee_Menu.txt", "w")
            for line in lines:
                if line.strip("\n") != del4_to_check:
                    f.write(line)
            f.close()
        else:
            del4_to_check = "            elif f == " + str(obj_no) + ":\n                c" + str(obj_no) + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country_origin + "\", " + str(avail_lvl_raw) + ")\n                print(c" + str(obj_no) + ".update())"
            f = open("coffee_Menu.txt", "r")
            lines = f.readlines()
            f = open("coffee_Menu.txt", "w")
            for line in lines:
                if line.strip("\n") != del4_to_check:
                    f.write(line)
            f.close()

    #  Delete a text
    del5_to_check = "{" + str(obj_no) + "}." + c_type + " Coffee        *{Price--------LKR." + str(price) + "}        *{Origin--------" + country_origin + "}        *{Available raw--------" + str(avail_lvl_raw) + "Kg}"
    f = open("coffee_Menu.txt", "r")
    lines = f.readlines()
    f = open("coffee_Menu.txt", "w")
    for line in lines:
        if line.strip("\n") != del5_to_check:
            f.write(line)
    f.close()


# -----------------------------------------------------For profiling-----------------------------------------------------------------------

def new_add_coffee_module():
    print("\n")
    print("\t\t\t\t\tWELCOME!")
    print("\n")
    print("-------------------**++--You're going to Add a new Coffee module!--++**-------------------")
    print("\n")
    obj_no = input("Enter Coffee type no: ")
    c_type = input("Enter Coffee type name: ")
    price = float(input("Enter the price: "))
    country_origin = input("Enter the country origin: ")
    avail_lvl_raw = float(input("Enter the amount of the raw material(Kg): "))
    #  Print after the '    # New Objects instantiate'
    o1_to_check = "    # New Objects instantiate"
    o1_to_add = str("    c" + str(obj_no) + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country_origin + "\", " + str(avail_lvl_raw) + ")")

    with open("cMachine.py", 'r+') as file_to_write:
        lines = file_to_write.readlines()
        file_to_write.seek(0)
        file_to_write.truncate()
        for line in lines:
            if line.startswith(o1_to_check):
                line = line.rstrip("\n") + "\n" + o1_to_add + "\n"
            file_to_write.write(line)
    file_to_write.close()

    #  Print after the 'Input new Objects'
    o1_to_check = "# Input new objects"
    o1_to_add = "        elif f == " + str(obj_no) + ":\n            c" + str(obj_no) + " = Coffee("'"' + c_type + '"'", " + str(price) + ", "'"' + country_origin + '"'", " + str(avail_lvl_raw) + ")\n            print(c" + str(obj_no) + ".availability_check())\n            c" + str(obj_no) + ".order()\n            print(c" + str(obj_no) + ".print_receipt(10))\n"

    with open("cMachine.py", 'r+') as file_to_write:
        lines = file_to_write.readlines()
        file_to_write.seek(0)
        file_to_write.truncate()
        for line in lines:
            if line.startswith(o1_to_check):
                line = line.rstrip("\n") + "\n" + o1_to_add + "\n"
            file_to_write.write(line)
    file_to_write.close()

    #  Print after the 'Insert new Objects1'
    o2_to_check = "# Insert new Objects1"
    o2_to_add = "            elif f == " + str(obj_no) + ":\n                c" + str(obj_no) + " = Coffee("'"' + c_type + '"'", " + str(price) + ", "'"' + country_origin + '"'", " + str(avail_lvl_raw) + ")\n                print(c" + str(obj_no) + ".availability_check())\n                print(c" + str(obj_no) + ".input_raw_materials())\n"

    with open("cMachine.py", 'r+') as file_to_write:
        lines = file_to_write.readlines()
        file_to_write.seek(0)
        file_to_write.truncate()
        for line in lines:
            if line.startswith(o2_to_check):
                line = line.rstrip("\n") + "\n" + o2_to_add + "\n"
            file_to_write.write(line)
    file_to_write.close()

    #  Print after the 'Insert new Objects2'
    o3_to_check = "# Insert new Objects2"
    o3_to_add = "            elif f == " + str(obj_no) + ":\n                c" + str(obj_no) + " = Coffee("'"' + c_type + '"'", " + str(price) + ", "'"' + country_origin + '"'", " + str(avail_lvl_raw) + ")\n                print(c" + str(obj_no) + ".update())\n"

    with open("cMachine.py", 'r+') as file_to_write:
        lines = file_to_write.readlines()
        file_to_write.seek(0)
        file_to_write.truncate()
        for line in lines:
            if line.startswith(o3_to_check):
                line = line.rstrip("\n") + "\n" + o3_to_add + "\n"
            file_to_write.write(line)
    file_to_write.close()

    f_append = open("coffee_Menu.txt", "a")
    f_append.write("\n{" + str(obj_no) + "}." + c_type + " Coffee        *{Price--------LKR." + str(price) + "}        *{Origin--------" + country_origin + "}        *{Available raw--------" + str(avail_lvl_raw) + "Kg}")
    f_append.close()

#  ---------------------------------------------------------------------------------------------------------------------


# ----------------------LOGICAL FUNCTION-del_coffee_module--------------------------------------------------------------
def new_del_coffee_module():
    print("\n")
    print("\t\t\t\t\tWELCOME!")
    print("\n")
    print("-------------------**++--You're going to Delete a new Coffee module!--++**-------------------")
    print("\n")
    obj_no = int(input("Enter Coffee type no: "))
    c_type = input("Enter Coffee type name: ")
    price = float(input("Enter the price: "))
    country_origin = input("Enter the country origin: ")
    avail_lvl_raw = float(input("Enter the amount of the raw material(Kg): "))

    #  Delete a text
    del1_to_check = "    c" + str(obj_no) + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country_origin + "\", " + str(avail_lvl_raw) + ")"
    with open("cMachine.py", 'r+') as file_to_write:
        f = open("coffee_Menu.txt", "r")
        lines = f.readlines()
        f = open("coffee_Menu.txt", "w")
        for line in lines:
            if line.strip("\n") != del1_to_check:
                f.write(line)
        f.close()

    #  Delete a text
    if obj_no == 1:
        del2_to_check = "        if f == " + str(obj_no) + ":\n            c" + str(obj_no) + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country_origin + "\", " + str(avail_lvl_raw) + ")\n            print(c" + str(obj_no) + ".availability_check())\n            c" + str(obj_no) + ".order()\n            print(c" + str(obj_no) + ".print_receipt(10))"
        f = open("coffee_Menu.txt", "r")
        lines = f.readlines()
        f = open("coffee_Menu.txt", "w")
        for line in lines:
            if line.strip("\n") != del2_to_check:
                f.write(line)
        f.close()
    else:
        del2_to_check = "        elif f == " + str(obj_no) + ":\n            c" + str(obj_no) + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country_origin + "\", " + str(avail_lvl_raw) + ")\n            print(c" + str(obj_no) + ".availability_check())\n            c" + str(obj_no) + ".order()\n            print(c" + str(obj_no) + ".print_receipt(10))"
        f = open("coffee_Menu.txt", "r")
        lines = f.readlines()
        f = open("coffee_Menu.txt", "w")
        for line in lines:
            if line.strip("\n") != del2_to_check:
                f.write(line)
        f.close()

    #  Delete a text
    if obj_no == 1:
        del3_to_check = "            if f == " + str(obj_no) + ":\n                c" + str(obj_no) + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country_origin + "\", " + str(avail_lvl_raw) + ")\n                print(c" + str(obj_no) + ".availability_check())\n                print(c" + str(obj_no) + ".input_raw_materials())"
        f = open("coffee_Menu.txt", "r")
        lines = f.readlines()
        f = open("coffee_Menu.txt", "w")
        for line in lines:
            if line.strip("\n") != del3_to_check:
                f.write(line)
        f.close()
    else:
        del3_to_check = "            elif f == " + str(obj_no) + ":\n                c" + str(obj_no) + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country_origin + "\", " + str(avail_lvl_raw) + ")\n                print(c" + str(obj_no) + ".availability_check())\n                print(c" + str(obj_no) + ".input_raw_materials())"
        with open("cMachine.py", 'r+') as file_to_write:
            f = open("coffee_Menu.txt", "r")
            lines = f.readlines()
            f = open("coffee_Menu.txt", "w")
            for line in lines:
                if line.strip("\n") != del3_to_check:
                    f.write(line)
            f.close()

    #  Delete a text
        if obj_no == 1:
            del4_to_check = "            if f == " + str(obj_no) + ":\n                c" + str(obj_no) + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country_origin + "\", " + str(avail_lvl_raw) + ")\n                print(c" + str(obj_no) + ".update())"
            f = open("coffee_Menu.txt", "r")
            lines = f.readlines()
            f = open("coffee_Menu.txt", "w")
            for line in lines:
                if line.strip("\n") != del4_to_check:
                    f.write(line)
            f.close()
        else:
            del4_to_check = "            elif f == " + str(obj_no) + ":\n                c" + str(obj_no) + " = Coffee(\"" + c_type + "\", " + str(price) + ", \"" + country_origin + "\", " + str(avail_lvl_raw) + ")\n                print(c" + str(obj_no) + ".update())"
            f = open("coffee_Menu.txt", "r")
            lines = f.readlines()
            f = open("coffee_Menu.txt", "w")
            for line in lines:
                if line.strip("\n") != del4_to_check:
                    f.write(line)
            f.close()

    #  Delete a text
    del5_to_check = "{" + str(obj_no) + "}." + c_type + " Coffee        *{Price--------LKR." + str(price) + "}        *{Origin--------" + country_origin + "}        *{Available raw--------" + str(avail_lvl_raw) + "Kg}"
    f = open("coffee_Menu.txt", "r")
    lines = f.readlines()
    f = open("coffee_Menu.txt", "w")
    for line in lines:
        if line.strip("\n") != del5_to_check:
            f.write(line)
    f.close()
