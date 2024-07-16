# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 14:00:42 2024

@author: Arjun
"""


def countBits(num):
    def bitCount(n):
        count = 0
        
        while(n):
            n &= n -1
            count += 1
        return count
    
    arr = []
    for i in range(num+1):
        arr.append(bitCount(i))
    return arr

print(countBits(5))
    
    
    
    
"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""