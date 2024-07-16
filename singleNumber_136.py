# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 18:33:56 2024

@author: Arjun
"""
class Solution:
    def singleNumber(self, nums):
        m={}
        
        for n in nums:
            m[n] = m.get(n,0)+1
        
        for i, v in m.items():
            if v == 1:
                return i
        return 0
        
"""
136. Single Number
Easy
Topics
Companies
Hint
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""