from tool import clearCMD, banner


def openIntro():
    print("+------------------------+")
    print(" No | Subjects")
    print("+------------------------+")
    file = open("Database-File/list_subject.txt", "r")
    i = 1
    for line in file:
        j = f"{i}".ljust(3)
        print(f" {j}| {line.strip()}")
        i += 1
    file.close()
    listSub = []
    with open("Database-File/list_subject.txt", "r") as file:
        listSub = [line.strip() for line in file]
    sub = int(input("\nChoose Sub : "))
    clearCMD()
    banner()
    print(listSub[sub - 1])


def openOption():
    print("\n1. Add Data\n2. Edit Data\n3. Remove Data\n")
    openOpt = input("=> ")
