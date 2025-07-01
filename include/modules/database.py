import sqlite3


class DataBase:
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

    def add_to(self, data, tare=False):
        keys_ = ', '.join(key for key in data.keys())
        values_ = tuple(data.values())
        placeholders_ = ', '.join(["?"] * len(data))

        query = f"INSERT OR REPLACE INTO drinks ({keys_}) VALUES ({placeholders_})"
        if tare:
            query = f"INSERT OR REPLACE INTO tare ({keys_}) VALUES ({placeholders_})"
        
        return self._connection(query, values_)

if __name__ == "__main__":
    # dict_ = {
    #     "barcode": '1111111112',
    #     "drink_name": "Արարատ",
    #     "bottle_weight": 800,
    #     "density": 0.910
    # }
    barcode = '18000000313'
    db = DataBase('bar_base.db')
    data = db.select(barcode, 1)
    print(dict(data))
