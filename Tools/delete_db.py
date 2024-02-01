import time


def removeData(listSub, sub):
    while True:
        with open(f"Database-File/{listSub[sub-1]}.txt", "r") as file:
            lines = file.readlines()
        with open(f"Database-File/{listSub[sub-1]}.txt", "w") as file:
            whatRemove = input("Choose index to delete data: ")
            for line in lines:
                if line.startswith(whatRemove) == False:
                    file.write(line)
                else:
                    file.write("\n")
        break
