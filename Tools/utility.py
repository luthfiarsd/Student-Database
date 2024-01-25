import os


def banner():
    print(f"+{'-'*80}+")
    welcomesign1 = "{:^82}".format("WELCOME TO")
    welcomesign2 = "{:^82}".format("STUDENT DATABASE")
    print(welcomesign1)
    print(welcomesign2)
    print(f"+{'-'*80}+")
    print()


def clearCMD():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
