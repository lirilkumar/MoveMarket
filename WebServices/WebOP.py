class WebOperation:
    @staticmethod
    def fetchSymbolData(symbol,from_date,to_date):
        import nsepy
        import time
        t1=time.time()
        print("fetching data from ",from_date," to ",to_date,"for ",symbol)
        symbol_data = nsepy.get_history(symbol, from_date ,to_date )
        print("found records for ",symbol,symbol_data.shape," in ",time.time()-t1,"Seconds")
        return symbol_data
