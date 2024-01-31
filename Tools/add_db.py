from .utility import clearCMD, banner
import time

def addData(listSub, sub):
    while True:
        try:
            clearCMD()
            banner()
            print("Press enter to cancel\n")
            nameData = input("Name             : ")
            if nameData=="":
                break
            actScore = int(input("Activity Score   : "))
            asgnScore = int(input("Assignment Score : "))
            examScore = int(input("Exam Score       : "))
            finalScore = (actScore + asgnScore + examScore) / 3
            with open(f"Database-File/{listSub[sub-1]}.txt", "r") as file:
                checkEnter = file.read()
                indexData = checkEnter.count("\n") + 1
            with open(f"Database-File/{listSub[sub-1]}.txt", "a") as file:
                file.write(f"MHS-{str(indexData)}" + ",")
                file.write(nameData + ",")
                file.write(str(actScore) + ",")
                file.write(str(asgnScore) + ",")
                file.write(str(examScore) + ",")
                file.write(str(finalScore) + "\n")
            isContinue = input("Continue? (y/n)\n\n=> ")
            if isContinue != "y":
                break
        except:
            print("Invalid input.")
            time.sleep(2)
