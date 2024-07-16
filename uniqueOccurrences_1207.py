# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 13:33:33 2024

@author: Arjun
"""
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        m = { x : 0 for x in set(arr)}
        
        for x in arr:
            m[x] += 1
            
        return len(set(m.values())) == len(m.values())
    
o = Solution()
print("Unique occurences ", o.uniqueOccurrences([1,2,2,1,1,3]))
print("Unique occurences ", o.uniqueOccurrences([1,2]))
        
        
"""
1207. Unique Number of Occurrences
Easy
Topics
Companies
Hint
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""