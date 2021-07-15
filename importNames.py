# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 13:31:05 2021

@author: muppabh
"""

import random
import names
import string

print(names.get_first_name())

first_names = []
last_names = []
full_names = []

def generate_userid_password(first_names_temp,last_names_temp):
    userid_temp = last_names_temp[:3:1] + first_names_temp[:3] + str(random.randint(1,20))
#   password_temp = ''.join(random.sample(string.ascii_uppercase + string.ascii.digits + string.ascii.lowercase, 7))
#    print(password_temp)
    charc_set = string.ascii_uppercase + string.digits + string.ascii_lowercase
    print(charc_set)
    values=random.sample(charc_set, 7)
    print(values)
    password = ''.join(values)
    print(password)
    return userid_temp.lower(),password


for i in range(1,11):  # loops 10 times from 1 to 10, 11 is exclusive here
    first_names_temp = names.get_first_name()
    first_names.append(first_names_temp)
    
    last_names_temp = names.get_last_name()
    last_names.append(last_names_temp)
    
    full_names_temp = last_names_temp + first_names_temp
    full_names.append(full_names_temp) 
    
    results = generate_userid_password(first_names_temp,last_names_temp)
    print(results)
       
print("first_names = {}\n".format(first_names))
print("last_names = {}\n".format(last_names))
print("full_names = {}\n".format(full_names))

