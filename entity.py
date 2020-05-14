from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import json

Base = declarative_base()


class Elev(Base):
    __tablename__ = 'elev'
    id = Column(Integer, primary_key=True)
    nume_elev = Column(String)
    clasa = Column(String)

    absente = relationship('Absenta', backref='elev', cascade="all, delete, delete-orphan")
    note = relationship('Nota', backref='elev', cascade="all, delete, delete-orphan")

    def getJson(self):
        return json.dumps( self.getJsonRaw() )

    def getJsonRaw(self):
        return {'id':self.id, 'nume':self.nume_elev, 'clasa':self.clasa}

    def verify(self):
        try:
            (year_str, grade) = self.clasa.split('-')
            year = int(year_str)
            if year < 1 or year > 12:
                raise ValueError('An incorect')
            if len(grade) != 1 or not grade.isalpha() or grade!=grade.lower():
                raise ValueError('Clasa incorecta')
        except:
            return False

        return True

    def __init__(self, *args,**kwargs):
        self.id = kwargs.get('id')
        self.nume_elev = kwargs.get('nume_elev')
        self.clasa = kwargs.get('clasa').lower()

        if not self.verify():
            raise Exception('Elev declarat gresit')


class Disciplina(Base):
    __tablename__ = 'disciplina'
    id = Column(Integer, primary_key=True)
    nume_disciplina = Column(String)
    profesor = Column(String)

    absente = relationship('Absenta', backref='disciplina', cascade="all, delete, delete-orphan")
    note = relationship('Nota', backref='disciplina', cascade="all, delete, delete-orphan")

    def getJson(self):
        return json.dumps( self.getJsonRaw() )

    def getJsonRaw(self):
        return {'id':self.id, 'denumire':self.nume_disciplina, 'profesor':self.profesor}

class Absenta(Base):
    __tablename__ = 'absente'
    id = Column(Integer, primary_key=True)
    code = Column(Integer, ForeignKey('elev.id'))
    codd = Column(Integer, ForeignKey('disciplina.id'))
    dataa = Column(Date)

    def getJson(self):
        return json.dumps( self.getJsonRaw() )

    def getJsonRaw(self):
        return {'id':self.id, 'elev':self.elev.getJsonRaw(), 'disciplina':self.disciplina.getJsonRaw(), 'data':self.dataa.__str__()}

class Nota(Base):
    __tablename__ = 'elev_disciplina'
    id = Column(Integer, primary_key=True)
    code = Column(Integer, ForeignKey('elev.id'))
    codd = Column(Integer, ForeignKey('disciplina.id'))
    data = Column(Date)
    nota = Column(Integer)

    def getJson(self):
        return json.dumps( self.getJsonRaw() )

    def getJsonRaw(self):
        return {'id': self.id, 'elev': self.elev.getJsonRaw(), 'disciplina': self.disciplina.getJsonRaw(), 'data': self.data.__str__(), 'nota':self.nota}