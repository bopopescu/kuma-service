import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import sys


class DB:
    def __init__(self):
        try:
            self.__engine = db.create_engine('mysql+mysqlconnector://root:@localhost/scoala')
            connection = self.__engine.connect()

            self.connect()
        except:
            print("Eroare la conectare", file=sys.stderr)

    def connect(self):
        Session = sessionmaker()
        Session.configure(bind=self.__engine)
        self.__session = Session()

    def disconnect(self):
        try:
            self.__session.close()
        except:
            print("Eroare la deconectare", file=sys.stderr)

    def query(self, type):
        return self.__session.query(type)

    def add(self, new):
        self.__session.add(new)

    def delete(self, old):
        self.__session.delete(old)

    def commit(self):
        self.__session.commit()

    def rollback(self):
        self.__session.rollback()

    def __del__(self):
        self.disconnect()