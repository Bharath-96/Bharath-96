# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 11:54:26 2021

@author: muppabh
"""

import random

print(random.random())  # prints random b/w 0 to 1
print(random.uniform(1,10))  # prints randoms b/w 1 to 10 floating points
a = random.randint(1, 20)
print(a)
print(random.randrange(1,5,1))
print(int(random.uniform(1,5)))

colors = ["Red", "Blue", "Orange", "White"]
print(random.choices(colors, k = 2))
print(random.choice(colors))

deck = list(range(1,53))
print(deck)

rand = random.shuffle(deck) # it wont print duplicate randoms values
print(rand)

hand = random.sample(deck, k=5) # it prints sample 5 unique deck 
print(hand)

phone = f'+91-{random.randint(9000000000,9999999999)}' # f string concept to concareate the stings data
print(phone)