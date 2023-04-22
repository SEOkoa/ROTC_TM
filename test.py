import os, sys, pandas as pd 
 
path = 'Members/62기 명단.xlsx'
 
df = pd.read_excel(path, header = 0)
print(df)