#!/usr/bin/env python3

from colorama import Fore, Style, init
from include.symbols import CLIPBOARD, ERROR, REPEAT, INBOX, ARROW



init()

def full_weigth() -> int:
	weight = input(Fore.GREEN + f"Ընդհանուր քաշը(գր) {CLIPBOARD} " + Style.RESET_ALL)
	while not weight.isdigit():
		print(Fore.RED + f"{ERROR} Սխալ Արժեք... {ARROW} \n" + Style.RESET_ALL )
		weight = input(Fore.GREEN + f"{REPEAT} Ընդհանուր քաշը(ԳՐ) {CLIPBOARD} " + Style.RESET_ALL)
	return int(weight)
	


def check_barcode_length() -> str:
	barcode = input(Fore.GREEN +f"Մուտքագրեք բարկոդը {INBOX} " + Style.RESET_ALL)

	while not (barcode.isdigit() and len(barcode) >= 11):
		barcode = input( Fore.RED + f"{REPEAT} Սխալ Բարկոդ {INBOX} " + Style.RESET_ALL)
	return str(barcode)
