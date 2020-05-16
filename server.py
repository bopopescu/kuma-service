from flask import Flask, render_template, request
from db import DB
from entity import Elev, Absenta, Disciplina, Nota

from repo import Elevi, Discipline, Absente, Note
from datetime import datetime

'''
Studenti: Evidenta rezultatelor la examene:
* Introducere / stergere / modificare studenti
* Introducere /stergere / modificare materii
* Introducere / modificare note
* Listari cataloage
'''

app = Flask(__name__)
db = DB()

elevRepo = Elevi(db)
discRepo = Discipline(db)
abstRepo = Absente(db)
noteRepo = Note(db)


@app.route("/", methods=['POST'])
def postIndex():
    response = {}
    response["response"] = "success"
    return response


@app.route("/", methods=['GET'])
def getIndex():
    return render_template('nav.html', title='Home')


@app.route("/elevi", methods=['GET', 'POST'])
def getElevi():
    elevi = elevRepo.getElevi()
    jsonData = []
    for elev in elevi:
        jsonData.append(elev.getJsonRaw())
    return {"elevi":jsonData}


@app.route("/elevi/c<clasa>", methods=['GET', 'POST'])
def getElevByClasa(clasa):
    elevi = elevRepo.getElevByClasa(clasa)
    jsonData = []
    for elev in elevi:
        jsonData.append(elev.getJsonRaw())
    return {"elevi":jsonData}


@app.route("/elevi/<id>", methods=['GET', 'POST'])
def getElevById(id):
    elev = elevRepo.getElevById(id)
    try:
        return {"elevi":elev[0].getJsonRaw()}
    except:
        return ""


@app.route("/elevi/insert", methods=['POST'])
def addElev():
    response = {}

    try:
        elev = Elev(nume_elev=request.values.get('nume'), clasa=request.values.get('clasa'))
        elevRepo.addElev(elev)

        response["response"] = "success"
        db.commit()
    except:
        response["response"] = "failure"
    finally:
        return response


@app.route("/elevi/update", methods=['POST'])
def setElev():
    response = {}

    try:
        elev = elevRepo.getElevById(request.values.get('id'))[0]
        elev.nume_elev = request.values.get('nume')
        elev.clasa = request.values.get('clasa')

        response["response"] = "success"
        db.commit()
    except:
        response["response"] = "failure"
    finally:
        return response


@app.route("/elevi/remove", methods=['POST'])
def dropElev():
    response = {}

    try:
        elev = elevRepo.getElevById(request.values.get('id'))[0]
        elevRepo.delElev(elev)

        response["response"] = "success"
        db.commit()
    except:
        response["response"] = "failure"
    finally:
        return response


@app.route("/discipline", methods=['GET', 'POST'])
def getDiscipline():
    disci = discRepo.getDiscipline()
    jsonData = []
    for disc in disci:
        jsonData.append(disc.getJsonRaw())
    return {"discipline":jsonData}


@app.route("/discipline/<id>", methods=['GET', 'POST'])
def getDisciplina(id):
    disc = discRepo.getDisciplinaById(id)
    try:
        return {"discipline":disc[0].getJsonRaw()}
    except:
        return ""


@app.route("/discipline/insert", methods=['POST'])
def addDisciplina():
    response = {}

    try:
        disc = Disciplina( nume_disciplina=request.values.get('denumire'), profesor=request.values.get('profesor') )
        discRepo.addDisciplina(disc)

        response["response"] = "success"
        db.commit()
    except:
        response["response"] = "failure"
    finally:
        return response


@app.route("/discipline/update", methods=['POST'])
def setDisciplina():
    response = {}

    try:
        disc = discRepo.getDisciplinaById(request.values.get('id'))[0]
        disc.nume_disciplina = request.values.get('denumire')
        disc.profesor = request.values.get('profesor')

        response["response"] = "success"
        db.commit()
    except:
        response["response"] = "failure"
    finally:
        return response


@app.route("/discipline/remove", methods=['POST'])
def dropDisciplina():
    response = {}

    try:
        disc = discRepo.getDisciplinaById(request.values.get('id'))[0]
        discRepo.delDisciplina(disc)

        response["response"] = "success"
        db.commit()
    except:
        response["response"] = "failure"
    finally:
        return response


@app.route("/note", methods=['GET', 'POST'])
def getNote():
    note = noteRepo.getNote()
    jsonData = []
    for nota in note:
        jsonData.append(nota.getJsonRaw())
    return {"note":jsonData}


@app.route("/note/<id>", methods=['GET', 'POST'])
def getNota(id):
    nota = noteRepo.getNotaById(id)
    try:
        return {"note":nota[0].getJsonRaw()}
    except:
        return ""


@app.route("/note/e<id>", methods=['GET', 'POST'])
def getNotaElev(id):
    elev = elevRepo.getElevById(id)
    try:
        note = noteRepo.getNotaByElev(elev[0])
        jsonData = []
        for nota in note:
            jsonData.append(nota.getJsonRaw())
        return {"note": jsonData}
    except:
        return ""


@app.route("/note/d<id>", methods=['GET', 'POST'])
def getNotaDisc(id):
    disc = discRepo.getDisciplinaById(id)
    try:
        note = noteRepo.getNotaByDisciplina(disc[0])
        jsonData = []
        for nota in note:
            jsonData.append(nota.getJsonRaw())
        return {"note": jsonData}
    except:
        return ""


@app.route("/note/insert", methods=['POST'])
def addNota():
    response = {}

    try:
        elev = elevRepo.getElevById( request.values.get('eid') )[0]
        disc = discRepo.getDisciplinaById( request.values.get('did') )[0]
        data = request.values.get('data')
        nota = Nota( elev=elev, disciplina=disc, data=data, nota=request.values.get('nota') )
        noteRepo.addNota(nota)

        response["response"] = "success"
        db.commit()
    except:
        response["response"] = "failure"
    finally:
        return response


@app.route("/note/update", methods=['POST'])
def setNota():
    response = {}

    try:
        nota = noteRepo.getNotaById( request.values.get('id') )[0]
        nota.elev = elevRepo.getElevById( request.values.get('eid') )[0]
        nota.disciplina = discRepo.getDisciplinaById( request.values.get('did') )[0]
        nota.data = request.values.get('data')
        nota.nota = request.values.get('nota')

        response["response"] = "success"
        db.commit()
    except:
        response["response"] = "failure"
    finally:
        return response


@app.route("/note/remove", methods=['POST'])
def dropNota():
    response = {}

    try:
        nota = noteRepo.getNotaById( request.values.get('id') )[0]
        noteRepo.delNota(nota)

        response["response"] = "success"
        db.commit()
    except:
        response["response"] = "failure"
    finally:
        return response


@app.route("/absente", methods=['GET', 'POST'])
def getAbsente():
    abste = abstRepo.getAbsente()
    jsonData = []
    for abst in abste:
        jsonData.append(abst.getJsonRaw())
    return {"absente":jsonData}


@app.route("/absente/<id>", methods=['GET', 'POST'])
def getAbsenta(id):
    abst = abstRepo.getAbsentaById(id)
    try:
        return {"absente":abst[0].getJsonRaw()}
    except:
        return ""


@app.route("/absente/e<id>", methods=['GET', 'POST'])
def getAbsentaElev(id):
    elev = elevRepo.getElevById(id)
    try:
        abste = abstRepo.getAbsentaByElev(elev[0])
        jsonData = []
        for abst in abste:
            jsonData.append(abst.getJsonRaw())
        return {"absente":jsonData}
    except:
        return ""


@app.route("/absente/d<id>", methods=['GET', 'POST'])
def getAbsentaDisc(id):
    disc = discRepo.getDisciplinaById(id)
    try:
        abste = abstRepo.getAbsentaByDisciplina(disc[0])
        jsonData = []
        for abst in abste:
            jsonData.append(abst.getJsonRaw())
        return {"absente":jsonData}
    except:
        return ""


@app.route("/catalog", methods=['GET', 'POST'])
def getClase():
    return {"clase":elevRepo.getClase()}


if __name__ == "__main__":
    app.run(port=8080)