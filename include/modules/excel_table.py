from  openpyxl import Workbook
import os
import shelve 
import datetime
wbook = Workbook()


class ExcelTable:

    def __init__(self):
        self.workbook = wbook.active
        # self.workbook_structure()
        

    def convert_and_save(self):
        self.workbook.append(["Անվանում", "Զտաքաշ"])
        db = self.read_from_shelve()
        self.from_shelve_to_excel(sh_db=db)

        if len(db) >= 1:
            wbook.save(f"invent_{datetime.datetime.now().strftime("%d-%m-%y")}.xlsx")
        

    def read_from_shelve(self):
        return shelve.open("buffer.db")
    
    def from_shelve_to_excel(self, sh_db):
        row = 2
        for name, weight in sh_db.items():
            self.workbook[f'A{row}'] = name
            self.workbook[f'B{row}'] = weight
            row += 1 
