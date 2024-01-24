import os


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
