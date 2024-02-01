from .add_db import addData


def editData(listSub, sub):
    with open(f"Database-File/{listSub[sub-1]}.txt", "r") as file:
        lines = file.readlines()
    with open(f"Database-File/{listSub[sub-1]}.txt", "w") as file:
        whatEdit = input("Choose index to edit data: ")
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
                file.write(f"MHS-{whatEdit}" + ",")
                file.write(nameData + ",")
                file.write(str(actScore) + ",")
                file.write(str(asgnScore) + ",")
                file.write(str(examScore) + ",")
                file.write(str(finalScore) + "\n")
