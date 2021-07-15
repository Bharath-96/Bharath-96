# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 20:09:04 2021

@author: muppabh
"""

def maximum(a, b):
        if a > b:
          print("hi")
          return a
     
        elif a < b:
            return b
        else:
            return 0
#a=input("Enter number1 : ")
#b=input("Enter number2 : ")

print(maximum(10, 20))

print(max(15,55))
list_of_no = [12, 13, 1, 14, 5, 50]
print(max(list_of_no))
list1 = [1, 2, 4, 5, 6, 10]
list2 = [40, 3, 5, 6]
print(max(list1 + list2))
print(min(list1 + list2))