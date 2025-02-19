# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 09:31:21 2024

@author: Arjun
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root,leaf):
            if not root:
                return 
            if not root.left and not root.right:
                leaf.append(root.val)
            dfs(root.left,leaf)
            dfs(root.right,leaf)
        
        leaf1,leaf2 = [],[]
        dfs(root1,leaf1)
        dfs(root2,leaf2)
        return leaf1 == leaf2
#        return self.getLeaf(root1) == self.getLeaf(root2)

#    def getLeaf(self, root: Optional[TreeNode]):
#        if root == None:
#            return None
#        left = self.getLeaf(root.left)
#        right = self.getLeaf(root.right)

#        if not right and not left:
#            return list([root.val])
#        elif not right and left:
#            return left
#        elif right and not left:
#            return right
#        elif right and left:
#            return left + right

"""
872. Leaf-Similar Trees
Solved
Easy
Topics
Companies
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
 

Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
"""