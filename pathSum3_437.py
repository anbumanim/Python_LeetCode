# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 10:35:36 2024

@author: Arjun
"""
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution:
    def __init__(self):
         self.paths = []
    def getPaths(self, node, path):
            # leaf
            if not node.left and not node.right:
                self.paths.append(path+[node.val])
                return
            
            # left only
            if node.left and not node.right:
                self.getPaths(node.left, path+[node.val])

            # right only
            if not node.left and node.right:
                self.getPaths(node.right, path+[node.val])

            # both present
            if node.left and node.right:
                self.getPaths(node.left, path+[node.val])
                self.getPaths(node.right, path+[node.val])

    def pathSum(self, root, targetSum: int) -> int:
        self.getPaths(root, [])
        print("At the end of getting paths: ")
        print(self.paths)
        return 0

o = Solution()

print("Sum = ", o.pathSum(root = [10,5,-3,3,2,None,11,3,-2,None,1], targetSum = 8))

        
"""
437. Path Sum III
Medium
Topics
Companies
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
"""