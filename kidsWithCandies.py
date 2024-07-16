# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:10:57 2024

@author: Arjun
"""

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ret = []
        maxVal = max(candies)
        
        for c in candies:
            if c+extraCandies >= maxVal:
                ret.append(True)
            else:
                ret.append(False)
        return ret
    
print(Solution().kidsWithCandies([2,3,4,5,1], 2))