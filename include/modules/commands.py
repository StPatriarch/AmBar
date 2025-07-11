#!/usr/bin/env python3

from include.modules.factory import Factory, PowderFactory, DrinkFactory
from include.modules.database import DataBase
from include.symbols import ERROR
from include.validations import check_barcode_length

# DataBase init
DB = DataBase('bar_base.db')


class Command:

    def __call__(self):
        self.filter_(db=DB)

    def __create(self, factory: Factory) -> None:
        return factory.calculation() or None


    def filter_(self, db: object) -> None:
        barcode = check_barcode_length()

        data = self._get_by_barcode(db, barcode)

        if data:
            factory = self.__define_factory(data)
            return self.__create(factory)

        else:
            self.__not_found_handle()

    def _get_by_barcode(self, db: object, barcode: str) -> dict:
        return  db.select(barcode) or db.select(barcode, 1)
    
    
    def __not_found_handle(self) -> None:
        print(f"{ERROR} Սխալ Բարկոդ | Բարկոդը չի գտնվել {ERROR}")
        print()

    def __define_factory(self, data: dict) -> Factory:
        if data['type'] == 'powder':
            return PowderFactory(data)
        else:
            return DrinkFactory(data)