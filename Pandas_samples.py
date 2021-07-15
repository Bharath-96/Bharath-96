# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 21:03:16 2021

@author: muppabh
"""

#Pandas Samples
import pandas as pd

mydataset={"class": [1,2,3,4,5],
           "students": [10,20,30,40,50]
          }
myout=pd.DataFrame(mydataset)
print(myout)

#version
print(pd.__version__)

list1=[1,2,3,4,5]
mylist=pd.Series(list1)
print(mylist)

print(mylist._values,type)
print(mylist.index)
print(mylist.dtype)
print(mylist.sum())
print(mylist.product())
print(mylist.mean())
##print(mylist.mode())
print(mylist.median())
print(mylist.max())

list2=["a","b","c","d","e"]
print(pd.Series(list1,list2))
print(pd.Series(data=list1, index=list2))

