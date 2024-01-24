import os
import time
import opendb as opdb
from tool import clearCMD, banner


while True:
    clearCMD()
    banner()

    print("Option:\n1. Open Subject Database\n2. Create Subject Database\n3. Exit\n")
    option = input("=> ")
    match option:
        case "1":
            # try:
            opdb.openIntro()
            opdb.openOption()
        # except:
        #     print("Database not found, please create a new one ...")
        #     time.sleep(2)
        #     continue
        case "2":
            print()
            nameSubject = input("Subject name : ")
            if os.path.exists(f"Database-File/{nameSubject}.txt"):
                print("Subject Exists!")
                time.sleep(1.5)
                continue
            else:
                with open(f"Database-File/{nameSubject}.txt", mode="w") as subject:
                    with open(
                        "Database-File/list_subject.txt", mode="a"
                    ) as listSubject:
                        listSubject.write(nameSubject + "\n")
                        print("Creating one ...")
                        time.sleep(1.5)
                        clearCMD()
                        banner()
                        print("Created.")
                        time.sleep(1.5)
                continue
        case _:
            break

    isContinue = input("\nContinue? (y/n)\n=> ")
    if isContinue != "y":
        break
