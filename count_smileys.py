# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:37:06 2024

@author: Arjun
"""
import re

def count_smileys(arr):
    mt = re.search(r"(\:\))", ":) :)")
    print("result is ", mt)
    pass #the number of valid smiley faces in array/list
    
def main():
    count_smileys(345)
main()    
# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces: ;( :> :} :]