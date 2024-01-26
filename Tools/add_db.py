from .utility import clearCMD, banner


def addData(listSub, sub):
    i = 1
    while True:
        clearCMD()
        banner()
        indexData = f"MHS-{i}"
        nameData = input("Name: ")
        actScore = int(input("Activity Score: "))
        asgnScore = int(input("Assignment Score: "))
        examScore = int(input("Exam Score: "))
        finalScore = (actScore + asgnScore + examScore) / 3
        with open(f"Database-File/{listSub[sub-1]}.txt", "a") as file:
            file.write(indexData + ",")
            file.write(nameData + ",")
            file.write(str(actScore) + ",")
            file.write(str(asgnScore) + ",")
            file.write(str(examScore) + ",")
            file.write(str(finalScore) + "\n")
        isContinue = input("Continue? (y/n)\n\n=> ")
        if isContinue != "y":
            break
        i += 1
