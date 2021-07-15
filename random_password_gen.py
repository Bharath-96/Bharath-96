# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 09:34:19 2021

@author: muppabh
"""

import random
import string

def random_gen_password():
    charc_set = string.ascii_uppercase + string.digits + string.ascii_lowercase
    print(charc_set)
    values=random.sample(charc_set, 7)
    print(values)
    password = ''.join(values)
    print(password)
    return password

def emp_id_to_password():
    
    emp_details = {"Bharath" : random_gen_password()}    
    print("Emp Name : {}".format(emp_details.keys()))
    print(emp_details.values())
    
random_gen_password()
emp_id_to_password()

## generate radom number between 1 - 20 and guess the number using while loop
n = 20
random_no_to_guessed = int(n * random.random()) + 1 # to get radom from 1-20
print(random_no_to_guessed)
no_to_enter = 0

while random_no_to_guessed != no_to_enter:
    no_to_enter = int(input(" Enter the guessed number : "))
    if no_to_enter > 0:
        if no_to_enter > random_no_to_guessed:
            print(" Enter number is larger")
        elif no_to_enter < random_no_to_guessed:
            print(" Enter numbr is smaller")
        else:
            print(" you guesses correct . Well done!")
    else:
        print(" sorry! enter greater than 0")
        