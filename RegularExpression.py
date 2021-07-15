# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 11:03:47 2021

@author: muppabh
"""
#regulrar expression 

import re

def checkemailpattern(pemail):
    repat = r"^([\w-\.]+)@([\w-\.]+)\.([a-zA-Z]{2,5})$"
    reobj = re.match(repat, pemail)
    if reobj:
        return reobj
    else:
        return False
    
def main():
    vemail = input('enter email: ')
    reobj = checkemailpattern(vemail)
    if reobj:
        print('\nMatched!', reobj.group())
    else:
        print('\nNo match found!')
        
main()