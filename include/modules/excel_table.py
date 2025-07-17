#!/usr/bin/env python3

# Մոդուլի նպատակն է բուֆերային տվյալներից գեներացնել վերջնական excel ֆայլը։

from include.modules.database import ShelveDataBase as shdb
from  openpyxl import Workbook
import datetime
wbook = Workbook()


class ExcelTable:

    def __init__(self):
        self.workbook = wbook.active
        

    def convert_and_save(self):
        self.workbook.append(["Անվանում", "Զտաքաշ"])
        db = shdb()._connection()

        if len(db) >= 1:
            row = 2
            for name, weight in db.items():
                self.workbook[f'A{row}'] = name
                self.workbook[f'B{row}'] = weight
                row += 1 

            wbook.save(f"invent_{datetime.datetime.now().strftime("%d-%m-%y")}.xlsx")
        
