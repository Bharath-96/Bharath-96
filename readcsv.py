# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 11:16:21 2021

@author: muppabh
"""
import pandas as pd
fileloc=r'C:\Users\muppabh\Documents\Bharath\readlist.csv'

csvlist=pd.read_csv(fileloc, skiprows=0)
print(csvlist)

a=pd.read_csv(fileloc)
#out=a.sort_values(ascending = False)
print(a.head(5))
print(a.tail(6))
print(a.to_string)
print(a.shape)
print(a.size)
print(a.max()
      
#b=pd.read_csv(filepath, usecols=['Name'])