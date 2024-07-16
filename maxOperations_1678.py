# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 19:35:57 2024

@author: Arjun
"""
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        myMap = {}
        count = 0
        for n in nums:
            if n >= k: continue
            if k-n in myMap:
                myMap[k-n] -= 1
                count += 1
                if myMap[k-n] == 0:
                    myMap.pop(k-n)
            else:
                if n in myMap:
                    myMap[n] += 1
                else:
                    myMap[n] = 1
        return count
o = Solution()
print(o.maxOperations([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3))
"""
1679. Max Number of K-Sum Pairs
Medium
Topics
Companies
Hint
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
"""