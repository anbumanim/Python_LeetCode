# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 18:13:17 2024

@author: Arjun
"""
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        
        for i in range(n):
            res.append(self.bitCount(i))
        return res
        
        
        def bitCount(self,n):
            count = 0
            while n > 0:
                n= n& n-1
                count += 1
            return count
        
"""
338. Counting Bits
Easy
Topics
Companies
Hint
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
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""
