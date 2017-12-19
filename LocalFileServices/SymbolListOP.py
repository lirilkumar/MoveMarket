class  SymbolListOperation:
    def __init__(self):
        print("Created")

    @staticmethod
    def getStockSymbols():
        import pandas
        from LocalFileServices.Config import Configuration

        location=Configuration.getSymbolListFileLocation()
        symbolList = pandas.read_csv(location, names=["SYMBOL","RATING","GOLDCHIP","PORTFOLIO-A"], encoding='utf-8',skiprows=1)
        print(symbolList)
        return symbolList

