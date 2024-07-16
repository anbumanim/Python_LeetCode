# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 13:23:10 2024

@author: Arjun
"""
def twoPointerSum(nums, target):
    one, two = 0,0
    sum = nums[0]
    
    while two < len(nums)-1:
        if sum < target:
            two += 1
            sum += nums[two]
        if sum == target:
            print("sum is reached with one=", one, " two=",two, " sum=", sum, " target=", target)
            return
        if sum > target:
            if one == two:
                two += 1
                sum += nums[two]
            else:
                sum -= nums[one]
                one += 1
    print("sum at the end is one=", one, " two=",two, " sum=", sum)
    
twoPointerSum([10, 5,3,3], 18)
twoPointerSum([10, -3,11], 8)
twoPointerSum([5,4,11,7], 22)
    
"""
547. Number of Provinces
Medium
Topics
Companies
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""