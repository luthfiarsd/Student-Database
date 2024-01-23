import os
import Manipulation as mnp

while True:
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

    print("+-------------------------------+")
    print("         STUDENT DATABASE        ")
    print("+-------------------------------+")

    print("Option:\n1. Add Data\n2. Remove Data\n3. Update Data\n4. Read Database\n")
    option = input("=> ")
    match option:
        case "1":
            pass  # add
        case "2":
            pass  # remove
        case "3":
            pass  # update
        case "4":
            from Manipulation import read
        case _:
            break

    isContinue = input("\nContinue? (y/n)\n=> ")
    if isContinue != "y":
        break
