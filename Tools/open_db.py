from .utility import clearCMD, banner
from . import add_db


def openIntro():
    while True:
        with open("Database-File/list_subject.txt", "r") as file:
            clearCMD()
            banner()
            print("Choose subject or press enter to go back: ")
            print("--------------------------")
            print(" No | Subjects")
            print("--------------------------")
            i = 1
            for line in file:
                j = f"{i}".ljust(3)
                print(f" {j}| {line.strip()}")
                i += 1
            listSub = []
            with open("Database-File/list_subject.txt", "r") as file:
                listSub = [line.strip() for line in file]
            try:
                sub = int(input("\n=> "))
            except:
                break
            x = True
            openSub(listSub, sub)
            print("\nOption:\n1. Add Data\n2. Edit Data\n3. Remove Data\n4. Back\n")
            openOpt = input("=> ")
            match openOpt:
                case "1":
                    add_db.addData(listSub, sub)
                case "2":
                    pass
                case "3":
                    pass
                case 4:
                    continue


def openSub(listSub, sub):
    clearCMD()
    banner()
    subjHeader = "{:^82}".format(f"+{'-'* (len(listSub[sub - 1]) + 2)}+")
    subjName = "{:^82}".format(f"| {listSub[sub - 1]} |")
    print(subjHeader)
    print(subjName)
    print(subjHeader)
    with open(f"Database-File/{listSub[sub-1]}.txt", "r") as file:
        header = " {:<6} | {:<40} | {:<5} | {:<5} | {:<5} | {:<5}".format(
            "Index", "Name", "Act", "Asgn", "Exam", "Final"
        )
        print("\n" + "-" * (len(header)) + "\n" + header + "\n" + "-" * (len(header)))
        lines = file.readlines()
        listing = []
        for line in lines:
            listing.append(line.split(","))
        for data in listing:
            dataPrint = " {:<6} | {:<40} | {:<5} | {:<5} | {:<5} | {:.2f}".format(
                data[0], data[1], data[2], data[3], data[4], float(data[5])
            )
            print(dataPrint)


# def openOption():
#     print("\n1. Add Data\n2. Edit Data\n3. Remove Data\n4. Back\n")
#     openOpt = input("=> ")
#     match openOpt:
#         case "1":
#             pass
#         case "2":
#             pass
#         case "3":
#             pass
