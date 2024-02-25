#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random

def roll_dice(num_rolls):
    for i in range(num_rolls):
        rolls_input = input("Enter the number of times to roll the dice: ")

        if rolls_input.isdigit():
            num_rolls = int(rolls_input)

            for i in range(num_rolls):
                die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
                total = die1 + die2
                print("Die 1: ",die1, "\nDie 2: ",die2,"\nTotal: ",total,"\n")
        else:
            print("Invalid input. Please enter a valid number.")
                      
roll_dice(1)


# In[ ]:




