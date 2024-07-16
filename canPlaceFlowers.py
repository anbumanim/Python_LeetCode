# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:38:21 2024

@author: Arjun
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        # convert list to string
        #strInp = "".join(str(i) for i in flowerbed)
        
        # count '000' in the string and return True if it is >= n
        #return strInp.count('000') >= n
        
        
        if n == 0: return True
        
        if len(flowerbed) == 1: 
            return True if n == 1 and flowerbed[0] == 0 else False
        
        count = 0
        # count both edge
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            count += 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            count += 1
            
        
        # count the place in the middle
        for i in range(1, len(flowerbed)-2):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                count += 1
                flowerbed[i] = 1
                
        
        return count >= n
    
#print(Solution().canPlaceFlowers([1,0,0,0,0,0,1], 2))
#print(Solution().canPlaceFlowers([0,0,1,0,1], 1))
#print(Solution().canPlaceFlowers([0], 1))
print(Solution().canPlaceFlowers([0,0,0,0,1],1))




"""
605. Can Place Flowers
Easy
Topics
Companies
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""