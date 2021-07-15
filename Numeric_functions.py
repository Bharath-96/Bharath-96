# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# define function for addition
def sum(x,y):
    print("x: {}".format(x))
    print("y: {}".format(y))
    print("sum of x,y ")
    z=x+y
    return z

# define function for difference
def diff(x,y):
    print("x: {}".format(x))
    print("y: {}".format(y))
    print("difference of x,y ")
    if x>=y:
        z=x-y
    else:
        z=y-x
    return z

# define Modular function
def mod(x,y):
    print("x: {}".format(x))
    print("y: {}".format(y))
    print("Modular of x,y ")    
    z=x/y
    return z

# define Reminder function
def rem(x,y):
    print("x: {}".format(x))
    print("y: {}".format(y))
    print("Remainder of x,y ")    
    z=x%y
    return z
    
x=10
y=4
add=sum(x,y)
print("= {}".format(add))
sub=diff(x,y)
print("= {}".format(sub))
modulus=mod(x,y)
print("= {}".format(modulus))
remainder=rem(x,y)
print("= {}".format(remainder))



#Name=input('Enter the Name : ')
#print("Name : {}".format(Name))

ctr=0
for row_nbr in range(1,5):
    print(row_nbr)
    ctr=ctr+row_nbr
else:
    print("sum of first {}".format(row_nbr),"Natural Numbers = {}".format(ctr))
    print(" Sum of first {} natural numbers = {}".format(row_nbr,ctr))
    my_string="Sum of first {} natural numbers = {}"
    print(my_string.format(row_nbr,ctr))
    
#Maximum of two or more Numbers in Python:
   
 
    