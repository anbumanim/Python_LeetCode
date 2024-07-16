# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 10:35:54 2023

@author: Arjun
"""

# Import Modules
import math
print(math.cos(30))
# print(cos(30))  # NameError: name 'cos' is not defined

# IMport ALL functions in Modules
from math import *
print(f"After import all moudles cos(30) + log(100) = {cos(30) + log(100)}")


# Import specific Functions
from math import cos, log
print(f"cos(30) + log(100) = {cos(30) + log(100)}")