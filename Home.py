from Utility.DateOP import DateOperation
from DatabaseOP.StockFileOP import FileOperation
from WebServices.WebOP import WebOperation
from datetime import date
import time
from LocalFileServices.SymbolListOP import SymbolListOperation


symbol_list=SymbolListOperation.getStockSymbols()
count=0

for symbol in symbol_list['SYMBOL']:
    symbol=str(symbol)
    print(symbol)
    # f=FileOperation(symbol)
    # f.start()
    # time.sleep(10)
    # f=None;


    