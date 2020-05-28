from entity import Elev, Absenta, Disciplina, Nota


class Elevi:
    def __init__(self, db):
        self.__db = db

    def getClase(self):
        clase = []
        elevi = self.__db.query(Elev).all()
        for elev in elevi:
            if not clase.__contains__(elev.clasa):
                clase.append(elev.clasa)
        return clase

    def getElevi(self):
        return self.__db.query(Elev).all()

    def getElevById(self, id):
        return self.__db.query(Elev).filter(Elev.id==id)

    def getElevByClasa(self, clasa):
        return self.__db.query(Elev).filter(Elev.clasa.ilike(clasa))

    def getElevByName(self, name):
        return self.__db.query(Elev).filter(Elev.nume_elev.ilike('%{}%'.format( name )))

    def addElev(self, elev):
        self.__db.add(elev)

    def delElev(self, elev):
        self.__db.delete(elev)


class Discipline:
    def __init__(self, db):
        self.__db = db

    def getDiscipline(self):
        return self.__db.query(Disciplina).all()

    def getDisciplinaById(self, id):
        return self.__db.query(Disciplina).filter(Disciplina.id==id)

    def getDisciplinaByProfesor(self, profesor):
        return self.__db.query(Disciplina).filter(Disciplina.profesor.ilike( '%{}%'.format( profesor )))

    def getDisciplinaByName(self, name):
        return self.__db.query(Disciplina).filter(Disciplina.nume_disciplina.ilike('%{}%'.format( name )))

    def addDisciplina(self, disciplina):
        self.__db.add(disciplina)

    def delDisciplina(self, disciplina):
        self.__db.delete(disciplina)


class Absente:
    def __init__(self, db):
        self.__db = db

    def getAbsente(self):
        return self.__db.query(Absenta).all()

    def getAbsentaById(self, id):
        return self.__db.query(Absenta).filter(Absenta.id==id)

    def getAbsentaByElev(self, elev):
        return self.__db.query(Absenta).filter(Absenta.elev==elev)

    def getAbsentaByDisciplina(self, disciplina):
        return self.__db.query(Absenta).filter(Absenta.disciplina==disciplina)

    def getAbsentaByDate(self, date):
        return self.__db.query(Absenta).filter(Absenta.dataa==date)

    def addAbsenta(self, absenta):
        self.__db.add(absenta)

    def delAbsenta(self, absenta):
        self.__db.delete(absenta)


class Note:
    def __init__(self, db):
        self.__db = db

    def getNote(self):
        return self.__db.query(Nota).all()

    def getNotaById(self, id):
        return self.__db.query(Nota).filter(Nota.id==id)

    def getNotaByElev(self, elev):
        return self.__db.query(Nota).filter(Nota.elev==elev)

    def getNotaByDisciplina(self, disciplina):
        return self.__db.query(Nota).filter(Nota.disciplina==disciplina)

    def getNotaByDisciplinaAndElev(self, disciplina, elev):
        return self.__db.query(Nota).filter(Nota.disciplina==disciplina).filter(Nota.elev==elev)

    def getNotaByDate(self, date):
        return self.__db.query(Nota).filter(Nota.data==date)

    def getNotaByNota(self, nota):
        return self.__db.query(Nota).filter(Nota.nota==nota)

    def addNota(self, absenta):
        self.__db.add(absenta)

    def delNota(self, absenta):
        self.__db.delete(absenta)