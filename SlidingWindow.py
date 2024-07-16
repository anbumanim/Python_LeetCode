# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 23:23:24 2024

@author: Arjun
"""

# Sliding window
str = "ADOBECODEBANC"
chars = "ABC"

found = {c:0 for c in chars}
    

start = int(0)
end = int(0)
missing = 3
shtStart = float("-inf")
shtEnd = float("inf")

while end < len(str):
    # case 1: Expand window
    if missing > 0:
        if str[end] in chars:
            found[str[end]] += 1
            if found[str[end]] == 1:
                missing -= 1
        end += 1
    
    # case 2: Solution found, update answer
    if missing == 0:
        # update answer
        if end - start < shtEnd - shtStart:
            shtStart, shtEnd = start, end

        # shrink window
        if str[start] in chars:
            found[str[start]] -= 1
            if found[str[start]] == 0:
                missing += 1
        start += 1
        
print("result is start = ", start, ", end = ",end, " result is ", str[start:end])
    
    
        
