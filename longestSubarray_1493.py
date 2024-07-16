# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 15:27:36 2024

@author: Arjun
"""
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zeroAdded = False
        zeroPos = -1
        
        start, end = 0,0
        
        while start < len(nums) and nums[start] == 0:
            start+=1
        
        if start == len(nums):
            return 0
        
        end = start
        maxLen = 0
        
        while end < len(nums):
            if nums[end] == 0:
                if zeroAdded:
                    start = zeroPos + 1
                else:
                    zeroAdded = True
                zeroPos = end
            maxLen = max(maxLen, end-start)
            end += 1
        
        # No 0's return len - 1
        if maxLen == len(nums):
            return len(nums) - 1
        return maxLen
        
o = Solution()
print("Max = ", o.longestSubarray([1,1,0,1])) 
print("Max = ", o.longestSubarray([0,1,1,1,1,1,0,1]))
print("Max = ", o.longestSubarray([0,0,0]))
print("Max = ", o.longestSubarray([0,0,1,1]))
print("Max = ", o.longestSubarray([0,0,1,1,0]))
        
        
"""
1493. Longest Subarray of 1's After Deleting One Element
Medium
Topics
Companies
Hint
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""