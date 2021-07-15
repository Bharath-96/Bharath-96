# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 10:32:26 2021

@author: muppabh
"""
#matstats.py module

TOTAL_MARKS = 1000
CUT_OFF_FOR_DISTINCTION = 80
CUT_OFF_FOR_PASS = 50
PERCENTAGE = 100

def percent_calcluator(*pMarks, pTotal = TOTAL_MARKS):
    vPassed, VDistinction = False, False
    Sum_of_Marks_obtained = sum(pMarks)
    print( "Sum of the Marks = {}".format(Sum_of_Marks_obtained))
    print( " Total Marks = {}".format(pTotal))
    vPercentage = ( Sum_of_Marks_obtained / pTotal ) * ( PERCENTAGE )
    print("percentage of Marks = {}".format(vPercentage))
    if vPercentage >= CUT_OFF_FOR_PASS:
        VDistinction = True
        if vPercentage >= CUT_OFF_FOR_DISTINCTION:
           vPassed = True
    return vPercentage, vPassed, VDistinction   
# Average of totl marks given 
def average_calculator(*pMarks):
    vAvg = ( sum(pMarks) )  / ( len(pMarks) ) 
    print( "average : {}".format(vAvg))
    return vAvg

#end of module
