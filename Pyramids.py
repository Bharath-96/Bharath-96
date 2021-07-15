# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 13:44:18 2021

@author: muppabh
"""

import random


n=5
k = 2*n - 2

for i in range(0,n): # outer loop to print number of rows
    for j in range(0,i+1):  # inner loop to print number of Columns
        print("*", end = "")
        
    print("\r")
        
for i in range(0,n): # outer loop to print number of rows
    for j in range(0, k):
        print(end = " ")
    k = k-2
    
    for j in range(0,i+1):  # inner loop to print number of Columns
        print("* ", end = "")
        
    print("\r")  # carriage return, moves cursor to next line 
