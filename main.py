#!/usr/bin/env python3
import signal
import sys
import os
from include.modules.commands import Command
from include.modules.excel_table import ExcelTable
from include.symbols import print_centered


def close_handler(sig, frame):
    file = ExcelTable()
    file.convert_and_save()
    print('Աշխատանքի ավարտ')
    sys.exit(0)
    
    



signal.signal(signal.SIGINT, close_handler)
signal.signal(signal.SIGTSTP, close_handler)




# GLOBALS
CMD = Command()

greet = '== ՁԵԶ Է ՈՂՋՅՈՒՆՈՒՄ ԲԱՐԻ ԻՎԵՆՏԱՐԻԶԱՑԻԱՅԻ ՀԱՇՎԻՉԸ =='



if __name__ == '__main__':
    print_centered(greet)
    if os.path.isfile('buffer.db'):
        os.remove('buffer.db')

    while True:
        CMD()


