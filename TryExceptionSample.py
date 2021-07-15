# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 13:02:00 2021

@author: muppabh
"""

def tryExcept_function(pNumberToDivide):
    try:
        DivedByNumber =int(input(" Enter the number to dive by  : "))
        DivideByResult = pNumberToDivide / DivedByNumber
        print( " DivideByResult = {}".format(DivideByResult))
        
    except NameError:
        print(" Please do verify the number use!")
        
    except ZeroDivisionError:
        print(" Division is not possible by zero ")
        
    except ValueError as e:
        print(" its value error , enter correct number", e)
        
    except Exception as e:
        print("Unknown Error", e)
        
    else:
        print( " No exceptions!")
        
    finally:
        print(" Execution Complete..")
        
tryExcept_function(200)
    