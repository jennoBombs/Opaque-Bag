#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Jennifer Reisinger"
__email__ = "jhubbard3@students.columbiabasin.edu"
__date__ = "Winter 2022"
__version__ = "0.1"

# You have an opaque bag full of 100 balls: 50 red, 30 green, and 20 blue. 
# Write a Python 3 function which picks a ball at random from a full bag and returns 
# the color as a string.

import random

def pick_ball():
    opaque_bag = ['red'] * 50 + ['green'] * 30 + ['blue'] * 20
    return random.choice(opaque_bag)


print(pick_ball())