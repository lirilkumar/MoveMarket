import threading
class FileOperation(threading.Thread):
    def __init__(self,symbol):
        threading.Thread.__init__(self)
        self.symbol=symbol
        print("created",self.symbol)
    def run(self):
        self.updateStockFileTillToday()
        # print ("running",self.symbol)
    def stockSymbolDatafileExist(self):
        from LocalFileServices.Config import Configuration
        from os import path
        location=Configuration.getStockDatabaseFilesLocation(self.symbol)
        return path.isfile(location)
    def saveStockDataToFile(self,symbol_data):
        import pandas
        from DatabaseOP import StockFileOP
        from LocalFileServices.Config import Configuration
        try:
            location=Configuration.getStockDatabaseFilesLocation(self.symbol)
            if(self.stockSymbolDatafileExist()):
                pandas.DataFrame.to_csv(symbol_data,path_or_buf=location,mode="a",header=False)
            else:
                pandas.DataFrame.to_csv(symbol_data,path_or_buf=location)
            print("Data Saved for",self.symbol)

        except Exception as e:
            print("error updating",e)
    def getLastUpdateDate(self):
        import pandas
        try:
            from LocalFileServices.Config import Configuration
            from datetime import date,timedelta
            if (self.stockSymbolDatafileExist()):
                location=Configuration.getStockDatabaseFilesLocation(self.symbol)
                symbol_data = pandas.read_csv(location,usecols=['Date'],keep_date_col=True)

                last_update_date=symbol_data[-1:]['Date'].values[0]
                dateChunks=last_update_date.split("-")
                # print(dateChunks,"date")
                last_update_date=date(int(dateChunks[0]),int(dateChunks[1]),int(dateChunks[2]))+timedelta(days=1)
            else:
                print("No File Found"+self.symbol)
                last_update_date=Configuration.getPastDateLimit()
            return  last_update_date
        except Exception as e:
            print("getLast Failed",self.symbol,e)
            return Configuration.getPastDateLimit()


    def getStockSymbolData(self,symbol,from_date,to_date):
        import pandas
        try:
            if (self.stockSymbolDatafileExist()):
                from LocalFileServices.Config import Configuration
                location=Configuration.getStockDatabaseFilesLocation(symbol)
                symbol_data=pandas.read_csv(location, encoding='utf-8')

                date_query='(Date>="'+from_date+'")'+'&'+'(Date<="'+to_date+'")'
                return symbol_data.query(date_query)
            else:
                return None
        except Exception as e:
            print("Error in fetching stock data",e)
            return None
    def updateStockFileTillToday(self):
        try:
            from WebServices import WebOP
            from Utility.DateOP import DateOperation
            symbol_data=WebOP.WebOperation.fetchSymbolData(self.symbol,self.getLastUpdateDate(),DateOperation.geTodayDate())
            self.saveStockDataToFile(symbol_data)
        except Exception as e:
            print(e,"found for ",self.symbol)