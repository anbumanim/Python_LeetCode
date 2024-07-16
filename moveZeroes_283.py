# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 15:58:26 2024

@author: Arjun
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = nums.count(0)
        for i in range(n):
            nums.remove(0)
            
        nums.extend([0] * n)
        
        return nums

o = Solution()
print(o.moveZeroes([0,1,0,3,12]))


"""
283. Move Zeroes
Easy
Topics
Companies
Hint
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?

Seen this question in a real interview before?
1/5
Yes
No
Accepted
3.1M
Submissions
5M
Acceptance Rate
61.8%
Topics
Companies
Hint 1
Hint 2
Similar Questions
Discussion (159)
"""
