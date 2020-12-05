#import libraries
import pandas as pd
import numpy as np

#get user input for ticker code
ticker=input('Enter ticker code:')

#get balance sheet
BS=pd.read_html('https://www.moneycontrol.com/financials/relianceindustries/balance-sheetVI/'+ticker+'#'+ticker,index_col=0,header=0)

#get profit & loss account
PL=pd.read_html('https://www.moneycontrol.com/financials/relianceindustries/profit-lossVI/'+ticker+'#'+ticker,index_col=0,header=0)

#Format extracted data
B/S1=BS[0]
BS1=BS1.replace(np.nan,0)
BS1 = BS1.apply(pd.to_numeric, errors='coerce', axis=1)
BS1.columns = BS1.columns.astype(str)

PL1=PL[0]
PL1=PL1.replace(np.nan,0)
PL1 = PL1.apply(pd.to_numeric, errors='coerce', axis=1)

#Print Balance Sheet & Profit & Loss account
print('Balance sheet of '+ticker)
print(BS1)

print('Profit & Loss Account of '+ticker)
print(PL1)

BS1.to_csv("filepath\filename.csv")
PL1.to_csv("filepath\filename.csv")

#Get specific values
a=input('Which value of the P&L do you want to view?  :')
b=input('Which year? Choose from:'+str(BS1.columns.to_list()))
b=str(b)
print(BS1.loc[a,b])
