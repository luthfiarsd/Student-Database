import os
import time
import Tools.opendb as opdb
from Tools.utility import clearCMD, banner


while True:
    clearCMD()
    banner()

    print("Option:\n1. Open Subject Database\n2. Create Subject Database\n3. Exit\n")
    option = input("=> ")
    match option:
        case "1":
            # try:
            x = True
            while x == True:
                clearCMD()
                banner()
                opdb.openIntro()
                listSub = []
                with open("Database-File/list_subject.txt", "r") as file:
                    listSub = [line.strip() for line in file]
                try:
                    sub = int(input("\n=> "))
                except:
                    break
                opdb.openSub(listSub, sub)
                print("\nOption:\n1. Add Data\n2. Edit Data\n3. Remove Data\n4. Back\n")
                openOpt = input("=> ")
                match openOpt:
                    case "1":
                        pass
                    case "2":
                        pass
                    case "3":
                        pass
                    case 4:
                        continue
        # except:
        #     print("Invalid input or database not found, please create a new one ...")
        #     time.sleep(2)
        #     continue
        case "2":
            print()
            nameSubject = input("Input subject name or press enter to cancel:\n\n=> ")
            if nameSubject == "":
                continue
            if os.path.exists(f"Database-File/{nameSubject}.txt"):
                print("Subject Exists!")
                time.sleep(2)
                continue
            else:
                with open(f"Database-File/{nameSubject}.txt", mode="w") as subject:
                    with open(
                        "Database-File/list_subject.txt", mode="a"
                    ) as listSubject:
                        listSubject.write(nameSubject + "\n")
                        print("Creating one ...")
                        time.sleep(2)
                        clearCMD()
                        banner()
                        print("Created.")
                        time.sleep(2)
                continue
        case _:
            break
