#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randint

class Dice:
    """ a class represents a single dice """
    def __init__(self, num_sides = 6):
        """ Assume a six-sides dice """
        self.num_sides = num_sides

    def roll(self):
        """ return a random value between 1 and number of sides """
        return randint(1, self.num_sides)
        

