# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:28:07 2024

@author: Arjun
"""
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        start = 0
        end = 0
        sum = 0.0
        
        while end < k:
            sum += nums[end]
            end+=1
        max = sum/k
        
        while end < len(nums):
            sum = sum - nums[start] + nums[end]
            
            if sum/k > max:
                max = sum/k
            start += 1
            end += 1
            
        return max

o = Solution()
#print("max is ", o.findMaxAverage([1,12,-5,-6,50,3], 4))
print("max is ", o.findMaxAverage([3,3,4,3,0], 3))

"""
643. Maximum Average Subarray I
Easy
Topics
Companies
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""