from .utility import clearCMD, banner


def openIntro():
    print("Choose subject or press enter to go back: ")
    print("--------------------------")
    print(" No | Subjects")
    print("--------------------------")
    with open("Database-File/list_subject.txt", "r") as file:
        i = 1
        for line in file:
            j = f"{i}".ljust(3)
            print(f" {j}| {line.strip()}")
            i += 1

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
        print(file.read())


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
