from db import DB
from entity import Elev, Absenta, Disciplina, Nota

from repo import Elevi, Discipline, Absente, Note
from datetime import datetime

import json

db = DB()

'''

elevi = db.query(Elev).all()

absente = db.query(Absenta).all()
for absenta in absente:
    print(absenta.elev.nume_elev, absenta.disciplina.nume_disciplina, absenta.dataa)

print()

note = db.query(Nota).all()
for nota in note:
    print(nota.elev.nume_elev, nota.disciplina.nume_disciplina, nota.nota, nota.data)

'''

elevRepo = Elevi(db)
discRepo = Discipline(db)
abstRepo = Absente(db)
noteRepo = Note(db)

elev_nou = Elev(id=1, nume_elev='Ionescu Ionel', clasa='11-D')
#elevRepo.addElev(elev_nou)

disc_nou = Disciplina(id=1, nume_disciplina="SOA", profesor='Cocu Adina')
#discRepo.addDisciplina(disc_nou)

abst_nou = Absenta(id=1, elev=elev_nou, disciplina=disc_nou, dataa=datetime.now().date() )
#abstRepo.addAbsenta(abst_nou)

nota_nou = Nota(id=1, elev=elev_nou, disciplina=disc_nou, data=datetime.now().date(), nota=7)
noteRepo.addNota(nota_nou)

elevi = elevRepo.getElevi()
disci = discRepo.getDiscipline()
abste = abstRepo.getAbsente()
notes = noteRepo.getNote()
'''
print("Elevi: ")
for elev in elevi:
    print(elev.id, elev.nume_elev, elev.clasa)

print("Discipline: ")
for disc in disci:
    print(disc.id, disc.nume_disciplina, disc.profesor)

print("Absente: ")
for abst in abste:
    print(abst.id, abst.elev.nume_elev, abst.disciplina.nume_disciplina, abst.dataa)

print("Note: ")
for nota in notes:
    print(nota.id, nota.elev.nume_elev, nota.disciplina.nume_disciplina, nota.data, nota.nota)

print("Dupa stergere: ")
#elevRepo.delElev(elev_nou)
#discRepo.delDisciplina(disc_nou)
abstRepo.delAbsenta(abst_nou)
noteRepo.delNota(nota_nou)


elevi = elevRepo.getElevi()
disci = discRepo.getDiscipline()
abste = abstRepo.getAbsente()
notes = noteRepo.getNote()
'''

print("Elevi: ")
for elev in elevi:
    #print(elev.id, elev.nume_elev, elev.clasa)
    print( elev.getJson() )

print("Discipline: ")
for disc in disci:
    #print(disc.id, disc.nume_disciplina, disc.profesor)
    print( disc.getJson() )

print("Absente: ")
for abst in abste:
    #print(abst.id, abst.elev.nume_elev, abst.disciplina.nume_disciplina, abst.dataa)
    print( abst.getJson() )

print("Note: ")
for nota in notes:
    #print(nota.id, nota.elev.nume_elev, nota.disciplina.nume_disciplina, nota.data, nota.nota)
    print(nota.getJson())