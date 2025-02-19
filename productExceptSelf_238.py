# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:56:11 2024

@author: Arjun
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        output = []
        
        # Compute left product array
        leftProd = [1]
        for i in range(1,len(nums)):
            leftProd.append(leftProd[i-1] * nums[i-1])

        # Compute right product array
        rightProd = [1]
        for i in range(len(nums)-1, -1, -1):
            rightProd.append(rightProd[i-1] * nums[i-1])

        
        for i in range(len(nums)):
            # Compute prefix products
            pre = 1
            for j in range(i):
                pre *= nums[j]
                
            # Compute suffix products
            suf = 1
            for j in range(i+1, len(nums)):
                suf *= nums[j]
            # Multiply them and assign it to output
            output.append(pre * suf)
            
        return output
    
o = Solution()  
print(o.productExceptSelf([1,-1,0,3,-3]))
#print(o.productExceptSelf([1,2,3,4]))

        
        


"""
238. Product of Array Except Self
Medium
Topics
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


Seen this question in a real interview before?
1/5
Yes
No
Accepted
2.7M
Submissions
4.1M
Acceptance Rate
66.4%
Topics
Companies
Hint 1
Think how you can efficiently utilize prefix and suffix products to calculate the product of all elements except self for each index. Can you pre-compute the prefix and suffix products in linear time to avoid redundant calculations?
"""
