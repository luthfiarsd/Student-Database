def openIntro():
    print("+------------------------+")
    print(" No | Subjects")
    print("+------------------------+")
    file = open("list_subject.txt", "r")
    i = 1
    for line in file:
        j = f"{i}".ljust(3)
        print(f" {j}| {line.strip()}")
        i += 1
    file.close()
    file = open("list_subject.txt", "r")
    file = open("list_subject.txt", "r")
    listSubject = file.readline()
    chooseFile = input("Choose file : ")
    if listSubject.strip() == chooseFile:
        print("mantap")
