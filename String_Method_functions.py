# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 17:45:44 2021

@author: muppabh
"""

#string
var="hello world"
var2="Bharath  "
print(var.capitalize())
print(var.title())
print(var.swapcase())
print(var.count('l'))
print(var2.strip())
print(var2.startswith('h'))
if "ar" in var2:
    print("found")
print("w" in var)
print("a" not in var2)
print(var2[:1:-1])
print(var2.replace("a","$"))

#List
vlist=[1,2,3,4,5,6,7,8]
print(vlist[0:vlist.index(8):2])
print(len(vlist))
print(vlist,type(vlist))
app=print(vlist.append("a"))
print(vlist)
print(vlist.pop())
print(vlist)
print(vlist.remove(3))
print(vlist)

name="firstname:Bharath middlename:Reddy lastname:Muppani"
vsplit=name.split(' ')
print(vsplit)
vjoin="|".join(vsplit)
print(vjoin)

#tuple
vtuple=("Bharath",24,"Male")

#dictionary
vdict={"Name": vtuple[0],"Age": vtuple[1],"Sex": vtuple[2]}
print("details of patient\n{}".format(vdict))
print(vdict.keys())
print(vdict.values())
print(vdict.items())

var={'class': (1,2,3,4,5),
     "":{
               "types":{"old":10,"young":2}
               }
     }
print(var)
print(var.get('three'))
print(var.get('class'))
print(var.keys())


    




