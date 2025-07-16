import sqlite3
import shelve
from abc import ABC, abstractmethod


class DataBaseManager(ABC):

    @abstractmethod
    def _connection():
        pass

    @abstractmethod
    def write_to():
        pass    



class SQLDataBase(DataBaseManager):
    def __init__(self, name):
        self.name = name
        self.connection = sqlite3.connect(self.name)

    def _connection(self, content, values=False):
        
        with self.connection:
            self.connection.row_factory = sqlite3.Row
            cursor_ = self.connection.cursor()
            cursor_.execute(content, values or [])
        return cursor_
    
    def select(self, barcode, tare=False):
        query = "SELECT * FROM drinks WHERE barcode = ?"
        if tare:
            query = "SELECT * FROM tare WHERE barcode = ?"

        return self._connection(query, (barcode,)).fetchone()

    def write_to(self, data, tare=False):
        keys_ = ', '.join(key for key in data.keys())
        values_ = tuple(data.values())
        placeholders_ = ', '.join(["?"] * len(data))

        query = f"INSERT OR REPLACE INTO drinks ({keys_}) VALUES ({placeholders_})"
        if tare:
            query = f"INSERT OR REPLACE INTO tare ({keys_}) VALUES ({placeholders_})"
        
        return self._connection(query, values_)


class ShelveDataBase(DataBaseManager):

    def _connection(self):
        return shelve.open("buffer.db")
    
    def write_to(self, name: str, weight: float) -> None:
        db = self._connection()
        db[name] = round(weight)
        db.close()