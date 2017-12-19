from datetime import date
class  Configuration:
    stock_data_location="E:/stocks/StockDataFiles/"
    symbol_data_location="E:/stocks/StockSymbol/full.csv"
    pastDateLimit=date(2015,1,1)

    @staticmethod
    def getStockDatabaseFilesLocation(symbol):
        return Configuration.stock_data_location+symbol+".csv"

    @staticmethod
    def getSymbolListFileLocation():
        return Configuration.symbol_data_location

    @staticmethod
    def getPastDateLimit():
        return Configuration.pastDateLimit