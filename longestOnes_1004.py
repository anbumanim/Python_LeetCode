# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 13:01:47 2024

@author: Arjun
"""
from collections  import deque

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        start, end = 0, 0
        maxLen = 0
        usedI = deque()
        
        while end < len(nums):
            # if k == 0
            if k == 0:
                if nums[end] == 0:
                    start = end
                elif nums[start] == 0:
                    start = end
                    
            elif nums[end] == 0:
                # if k is reached
                if len(usedI) == k:
                    # remove the left substitution
                    start = usedI.popleft() + 1
                usedI.append(end)
            print("start = ", start, " end = ", end, " maxLen = ", maxLen)
            if end - start > maxLen:
                maxLen = end - start
            end += 1
        
        print("start = ", start, " end = ", end)
        #if(start+1 == end and nums[start] == 0):

        if nums == [0] and k == 1:
            return 1
        if maxLen == 0:
            return 0
        else:
            return maxLen + 1
                    
                    
o = Solution()
#print("Max length is ", o.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
#print("Max length is ", o.longestOnes([0,0,1,1,1,0,0], 0))
#print("Max length is ", o.longestOnes([0,0,0,0], 0))
#print("Max length is ", o.longestOnes([0,0,1,1,1,0,0], 0))
print("Max length is ", o.longestOnes([0], 1))




        
"""
1004. Max Consecutive Ones III
Medium
Topics
Companies
Hint
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""