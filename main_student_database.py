import os
import time
import open_database as opdb


def banner():
    print("+-------------------------------+")
    print("           WELCOME TO            ")
    print("        STUDENT DATABASE         ")
    print("+-------------------------------+")
    print()


def clearCMD():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")


while True:
    clearCMD()
    banner()

    print("Option:\n1. Open Subject Database\n2. Create Subject Database\n")
    option = input("=> ")
    match option:
        case "1":
            # try:
            opdb.openIntro()
            # except:
            #     print("Database not found, please create a new one ...")
            #     time.sleep(2)
            #     continue
        case "2":
            print()
            nameSubject = input("Subject name : ")
            if os.path.exists(f"{nameSubject}.txt"):
                print("*Subject Exists*")
                time.sleep(1.5)
                continue
            else:
                subject = open(f"{nameSubject}.txt", mode="w")
                listSubject = open("list_subject.txt", mode="a")
                listSubject.write(nameSubject + "\n")
                print("Creating one ...")
                time.sleep(1.5)
                listSubject.close()
                subject.close()
                continue
        case _:
            break

    isContinue = input("\nContinue? (y/n)\n=> ")
    if isContinue != "y":
        break
