# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 19:49:02 2024

@author: Arjun
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.paths = []
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pVal = p.val
        qVal = q.val
        def findPath(node, path):
            #print("node=", node, " path = ", path )
            if not node.left and not node.right:
                self.paths.append(path + [node.val])
            if node.left:
                findPath(node.left, path + [node.val])
            if node.right:
                findPath(node.right, path + [node.val])
                
        findPath(root, [])
        #print(self.paths)

        # path contains p and q
        pPath = []
        qPath = []
        for path in self.paths:
            if pVal in path:
                pPath = path
                #print("pPath1 = ", pPath)
                if qPath:
                    break
            if qVal in path:
                qPath = path
                print("qPath1 = ", qPath)
                if pPath:
                    break
        
        # shortest path
        print("pPath = ", pPath)
        print("qPath = ", qPath)
        if pPath.index(pVal) <= qPath.index(qVal):
            print("pVal")
            for i in range(pPath.index(pVal)-1, -1, -1):
                print(pPath[i])
                if pPath[i] in qPath:
                    node = root
                    inx = 1
                    while node.val != pVal:
                        if node.left.val == pPath[inx]:
                            node = node.left
                            inx += 1
                        else:
                            node = node.right
                            inx += 1
                    return node
        else:
            print("qVal")
            for i in range(qPath.index(qVal)-1, -1, -1):
                print(qPath[i])
                if qPath[i] in pPath:
                    node = root
                    inx = 1
                    while node.val != qVal:
                        if node.left.val == qPath[inx]:
                            node = node.left
                            inx += 1
                        else:
                            node = node.right
                            inx += 1
                    return node

        
        
            
"""
236. Lowest Common Ancestor of a Binary Tree
Medium
Topics
Companies
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""