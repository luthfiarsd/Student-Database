import time
def removeData(listSub, sub):
    while True:
        with open(f"Database-File/{listSub[sub-1]}.txt", "r") as file:
            lines = file.readlines()
            print(lines)
        with open(f"Database-File/{listSub[sub-1]}.txt", "w") as file:
            whatRemove = input("Choose index to remove: ")
            for line in lines:
                if line.startswith(whatRemove)==False:
                    file.write(line)
        break
