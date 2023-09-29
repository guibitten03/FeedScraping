import sqlite3

from pathlib import Path




class Database():
    def __init__(self):
        pass


    def connect(self, db_name):
        '''
            Input: Database Name.
            Output: Connection Object and Database Cursos.
        '''

        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()


    def commit(self):
        self.con.commit()