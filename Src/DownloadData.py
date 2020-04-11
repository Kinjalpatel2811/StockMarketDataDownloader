import pandas as pd 
from  alpha_vantage.timeseries import TimeSeries

def GetData(symbol='INFY'):
        keyfile=open("keys",'r')
        API_KEY=keyfile.readline().rstrip()
        ts = TimeSeries(key=API_KEY,output_format='pandas')
        EXCHANGE="NSE"#I am Working With National Stock Exchange of India, You Need To change Exchange Accordingly
        data, meta_data = ts.get_daily(symbol=EXCHANGE+':'+symbol,outputsize='full')
        #AlphaVantage API returns Column Names with 1,2,3 which is not a standard way
        #So We Are Renaming Columns to Standard Names
        data.rename(columns = {'1. open':'open','2. high':'high','3. low':'low','4. close':'close','5. volume':'volume'}, inplace = True) 
        data.sort_values(by='date', ascending=True,inplace = True)
        return data

#Stock List Is the List Of Stocks for Which You Want to Download Data
# Sample Stock List Contains All FnO Stocks On NSE India    
df=pd.read_csv(r".\DataFiles\StockList.csv")
for i in range(len(df)) :  
    print("Downloading data of ",df.loc[i, "Symbol"])
    try:
        dfstockdata=GetData(symbol=df.loc[i, 'Symbol'])
        dfstockdata.to_csv('.\\DataFiles\\'+df.loc[i, "Symbol"]+'.csv')
        print("Successfully downloaded data  of ",df.loc[i, "Symbol"]) 
    except:
        print('Unable to Download data for ',df.loc[i, 'Symbol'])



