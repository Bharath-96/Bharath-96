# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 08:43:05 2021

@author: muppabh
"""

#Arguments types
#1. Required argument function
#2. Keyowrd argument fucntion
#3. Default argument function
#4. Variable argument function

#1. *********** Required argument function *************************
def req_arg_func(pvar1, pvar2):
    print(" *********** Required argument function ***********************")
    print(" Inside the fucntion arg1 : ", pvar1)
    print(" Inside the fucntion arg2 : ", pvar2)
    
vlist1 = [1,2,3,4]
vlist2 = ["Hello", "world"]
req_arg_func(vlist1, vlist2)

#2. *********** Keyword argument function *************************
def key_arg_func(pvar1, pvar2):
    print(" *********** Keyword argument function ***********************")
    print(" Inside the fucntion arg1 : ", pvar1)
    print(" Inside the fucntion arg2 : ", pvar2)
    

key_arg_func(pvar1= [1, 4, 5], pvar2= ["hello"])
key_arg_func([1, 6, 9], pvar2 = ["python"])

#3. *********** Default argument function *************************
def default_arg_func(pvar1 = [10, 20], pvar2 = ["good"]):
    print(" *********** Default argument function ***********************")
    print(" Inside the fucntion arg1 : ", pvar1)
    print(" Inside the fucntion arg2 : ", pvar2)
    

default_arg_func(pvar1= [1, 4, 5], pvar2= ["hello"])
default_arg_func(pvar2 = ["python"])
default_arg_func()

#4. *********** Variable argument function *************************
def var_arg_func(pName, *pMarks):
    print(" *********** Default argument function ***********************")
    print(" Inside the fucntion arg1 : ", pName)
    print(" Inside the fucntion arg2 : ", pMarks)
    pAvg = (sum(pMarks) / len(pMarks))
    print(" Avg marks for {} is {} ".format(pName, pAvg))
    
var_arg_func("Bharath", 10,20,30)

def test_fucn(pTest1, pTest2):
    pTest1 = [11, 22, 33]
    pTest2[1] = ["hello world"]
    print(" *********** fucntion test argument function ***********************")
    print(" Inside the fucntion arg1 : ", pTest1)
    print(" Inside the fucntion arg2 : ", pTest2)
pVar2 = [1, 2, 3, 4]    
pVar3 = ["Hello", "python"]
test_fucn(pVar2, pVar3)
print(" Outside the fucntion arg1 : ", pVar2)
print(" Outside the fucntion arg2 : ", pVar3)