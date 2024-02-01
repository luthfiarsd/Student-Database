from .utility import clearCMD, banner


def editData(listSub, sub):
    while True:
        with open(f"Database-File/{listSub[sub-1]}.txt", "r") as file:
            lines = file.readlines()
        whatEdit = input("Choose index to edit data: ")
        if whatEdit == "":
            break
        whatEditInt = "".join(c for c in whatEdit if c.isdigit())
        clearCMD()
        banner()
        with open(f"Database-File/{listSub[sub-1]}.txt", "w") as file:
            for line in lines:
                if line.startswith(whatEdit) == False:
                    file.write(line)
                else:
                    print("Press enter to cancel\n")
                    nameData = input("Name             : ")
                    if nameData == "":
                        break
                    actScore = int(input("Activity Score   : "))
                    asgnScore = int(input("Assignment Score : "))
                    examScore = int(input("Exam Score       : "))
                    finalScore = (actScore + asgnScore + examScore) / 3
                    file.write(f"MHS-{whatEditInt}" + ",")
                    file.write(nameData + ",")
                    file.write(str(actScore) + ",")
                    file.write(str(asgnScore) + ",")
                    file.write(str(examScore) + ",")
                    file.write(str(finalScore) + "\n")
            break
