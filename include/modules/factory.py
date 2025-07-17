#!/usr/bin/env python3

# Մոդուլի այս հատվածը առաջարկում է ապրանքի զտաքաշը հաշվարկելու համապատասխան լոգիկա կախված վերջինիս տեսակից։ 
# Խմիչքի դեպքում այն ընդհանուր քաշից հանում է տարայի քաշը ապա մնացորդը բաժանում խտության վրա իսկ այլ ապրանքի դեպքում այն 
# ընդհանուր քաշից կհանի միայն տարայինը։ Ծրագրում այս երկու լոգիակն տարանջատելու համար էլ կիրառվում է այս մոդուլը որը 
# ներկայացնում է իրենից ինֆորմատիկ֊ճարտարագիտական պատտերն որը, կոչվում է factory, այստեղից էլ մոդուլի անունը։


from include.modules.database import ShelveDataBase as shdb
from colorama import Fore, Style, init
from include.validations import full_weight
from include.symbols import JAR, DRINK, OUTBOX, RECYCLING
init()


class Factory:

    def __init__(self, data_base: object) -> None:
        self.data_base = data_base


    def calculation(self) -> None:
        raise NotImplementedError

    def full_weight_validation(self) -> int:
        return full_weight()
    

    def string_output_design(self, weight: float, type: str) -> None:
        print()
			
        print(Fore.RED + ("-" * 23) + "\\" + Style.RESET_ALL)

        print(f"ԶՏԱՔԱՇ {OUTBOX} {round((weight))} {type}.")

        print(Fore.RED + ("-" * 23) + "/" + Style.RESET_ALL)

        print()


class PowderFactory(Factory):

    def __init__(self, data):
        super().__init__(data_base=data)

    def calculation(self) -> None:

        print()
        print(Fore.CYAN + f"{self.data_base['tare_name']} {JAR}" + Style.RESET_ALL)
        print('-' * (len(self.data_base['tare_name']) + 4))

        while True:
            
            FULL_WEIGTH = self.full_weight_validation()
			
            TARE_WEIGTH = self.data_base['tare_weight']
				
            CLEAR_WEIGTH = FULL_WEIGTH - TARE_WEIGTH

            self.string_output_design(CLEAR_WEIGTH, 'գր․')
            # self.write_to_shelve(name=self.data_base['tare_name'], weight=CLEAR_WEIGTH)


class DrinkFactory(Factory):

    def __init__(self, data: object) -> None:
        super().__init__(data_base=data)


    def calculation(self) -> None:

        print()
        print(Fore.CYAN + f"{self.data_base['drink_name']} {DRINK}" + Style.RESET_ALL )
        print('-' * (len(self.data_base['drink_name']) + 4))
               
        FULL_WEIGTH = self.full_weight_validation()
			
        BOTTLE_WEIGTH = self.data_base['bottle_weight']
        DRINK_DENSITY = self.data_base['density']
			
			
        CLEAR_WEIGTH = (FULL_WEIGTH - BOTTLE_WEIGTH) / DRINK_DENSITY

        self.string_output_design(CLEAR_WEIGTH, 'մլ․')

        shdb().write_to(name=self.data_base['drink_name'], weight=CLEAR_WEIGTH)

        input(Fore.BLUE + f"{RECYCLING} ՇԱՐՈՒՆԱԿԵԼ {RECYCLING} " + Style.RESET_ALL) 

		





    
