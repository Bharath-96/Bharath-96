# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 13:01:07 2021

@author: muppabh
"""

import math
import random
import pandas
import numpy
import names

myData = ["Bharath","Sai","Jo","Bharath","Raj","Krish","Jo"]

empty_list = []
 
def Main():
    
    results = CountChoice_fun(myData, "bharath")
    print(results)
    
def CountChoice_fun(myData, UserChoice):  ### Function to get the counts of str occurence 
    for checkData in myData:
        temp = checkData.lower()
###        print(temp)
        empty_list.append(temp)
    return empty_list.count(UserChoice)

#print(empty_list.count("bharath"))
#print(empty_list[1].startswith("sai"))
    
Main()










    
    