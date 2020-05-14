from prettytable import PrettyTable
import requests
import json
import sys


def getClasses():
    r = requests.post('http://127.0.0.1:8080/catalog')
    catalog = json.loads(r.text)["clase"]

    printer = PrettyTable()
    printer.field_names = ["Id", "Clasa"]

    for id in range(len(catalog)):
        printer.add_row([id + 1, catalog[id]])

    print(printer)

    class_id = input("Enter class ID...")

    try:
        class_id = int(class_id)
        getClass( catalog[class_id-1] )
    except:
        return


def getDiscipline():
    r = requests.post('http://127.0.0.1:8080/discipline')
    discipline = json.loads(r.text)["discipline"]

    print("0 - pentru disciplina noua")

    printer = PrettyTable()
    printer.field_names = ["Id", "Denumire", "Profesor"]

    for id in range(len(discipline)):
        printer.add_row([id + 1, discipline[id]["denumire"], discipline[id]["profesor"]])

    print(printer)

    choice  = input("Enter discipline ID...")

    try:
        choice = int(choice)
        if choice == 0:
            addDisciplina()
        else:
            getDisciplina( discipline[choice-1] )
    except:
        return


def addDisciplina():
    data = {}
    data["denumire"] = input("Denumire disciplina...")
    data["profesor"] = input("Profesor disciplina...")

    r = requests.post('http://127.0.0.1:8080/discipline/insert', data)
    result = json.loads(r.text)["response"]

    if result=="success":
        getDiscipline()
    else:
        addDisciplina()


def getDisciplina( disc ):
    choice = input("r - remove\nu - update")
    data = {}
    data["id"] = disc["id"]

    if choice=="r":
        r = requests.post('http://127.0.0.1:8080/discipline/remove', data)
    elif choice=="u":
        data["denumire"] = input("Denumire disciplina({})...".format( disc["denumire"] ))
        data["profesor"] = input("Profesor disciplina({})...".format( disc["profesor"] ))
        if data["denumire"]=="":
            data["denumire"] = disc["denumire"]
        if data["profesor"] == "":
            data["profesor"] = disc["profesor"]
        r = requests.post('http://127.0.0.1:8080/discipline/update', data)

    getDiscipline()


def getClass(class_id):
    r = requests.post('http://127.0.0.1:8080/elevi/c'+class_id)
    catalog = json.loads(r.text)["elevi"]

    print("0 - pentru elev nou")

    printer = PrettyTable()
    printer.field_names = ["Id", "Nume", "Clasa"]

    for id in range(len(catalog)):
        printer.add_row([id+1, catalog[id]['nume'], catalog[id]['clasa']])

    print(printer)

    student_id = input("Enter student ID...")

    try:
        student_id = int(student_id)

        if student_id>0:
            print("g - grades")
            print("a - absences")
            print("u - update")
            print("r - remove")
            choice = input()

            if choice=="g":
                getNote( catalog[student_id-1]['id'] )
            elif choice=="a":
                getAbsente( catalog[student_id-1]['id'] )
            else:
                getElev( catalog[student_id-1], choice )
        else:
            addElev(class_id)
    except:
        return


def addElev(class_id):
    data = {}
    data["nume"] = input("Nume elev...")
    data["clasa"] = class_id

    r = requests.post('http://127.0.0.1:8080/elevi/insert', data)
    result = json.loads(r.text)["response"]

    if result=="success":
        getClass(class_id)
    else:
        addElev(class_id)


def getElev(student, choice):
    data = {}
    data["id"] = student["id"]

    if choice=="r":
        r = requests.post('http://127.0.0.1:8080/elevi/remove', data)
    elif choice=="u":
        data["nume"] = input("Nume elev({})...".format(student["nume"]))
        data["clasa"] = input("Clasa elev({})...".format(student["clasa"]))
        if data["nume"] == "":
            data["nume"] = student["nume"]
        if data["clasa"] == "":
            data["clasa"] = student["clasa"]
        r = requests.post('http://127.0.0.1:8080/elevi/update', data)

    getClass( data["clasa"] )


def getNote(elev_id):
    r = requests.post('http://127.0.0.1:8080/note/e{}'.format( elev_id ))
    note = json.loads(r.text)["note"]

    print("0 - pentru nota noua")

    printer = PrettyTable()
    printer.field_names = ["Id", "Nota", "Data", "Disciplina", "Profesor", "Elev", "Clasa"]

    for nota in note:
        printer.add_row([nota['id'], nota["nota"], nota["data"], nota['disciplina']["denumire"], nota['disciplina']["profesor"], nota['elev']["nume"], nota['elev']["clasa"]])

    print(printer)


def getAbsente(elev_id):
    r = requests.post('http://127.0.0.1:8080/absente/e{}'.format( elev_id ))
    absente = json.loads(r.text)["absente"]

    printer = PrettyTable()
    printer.field_names = ["Id", "Data", "Disciplina", "Profesor", "Elev", "Clasa"]

    for absenta in absente:
        printer.add_row([absenta['id'], absenta["data"], absenta['disciplina']["denumire"], absenta['disciplina']["profesor"], absenta['elev']["nume"], absenta['elev']["clasa"]])

    print(printer)


if __name__=="__main__":
    r = requests.post('http://127.0.0.1:8080')
    result = json.loads(r.text)["response"]

    if not result=="success":
        print("Connection error", file=sys.stderr)
    else:
        while True:
            print("d - pentru discipline")
            print("c - pentru clase")
            choice = input()

            if choice=="d":
                getDiscipline()
            elif choice=="c":
                getClasses()
            else:
                break
