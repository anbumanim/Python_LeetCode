# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 21:27:08 2024

@author: Arjun
"""

# Binary Search Tree operations in Python


# Create a node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
# insert a node
def insert(node, key):
    # save the original root
    root = node
    
    # if node is not present, create and return
    if not node:
        node = Node(key)
        print("Creating new node")
        return node
    
    # if the key is already present sent
    if node.key == key:
        return node
    
    while node:
        if node.key == key:
            print("key is already present")
            return root
        if node.key > key:
            if not node.left:
                node.left = Node(key)
                break
            node = node.left
        if node.key < key:
            if not node.right:
                node.right = Node(key)
                break
            node = node.right
    
    return root

# inorder
def inorder(root):
    if not root:
        return
    
    if root.left:
        inorder(root.left)

    print(root.key, "->", end=" ")
    
    if root.right:
        inorder(root.right)

# inorder reverse
def inorderReverse(root):
    if not root:
        return
    
    if root.right:
        inorderReverse(root.right)

    print(root.key, "<-", end=" ")
    
    if root.left:
        inorderReverse(root.left)


    
def printNode(node):
    print("[",end=" ")
    if not node:
        print("]")
        return
    
    level = [node]
    isNext = True
    while isNext:
        isNext = False
        nextLevel = []
        for n in level:
            if n:
                print(n.key, end=", ")
                nextLevel.append(n.left)
                nextLevel.append(n.right)

                if n.left or n.right:
                    isNext = True
            else:
                print("null", end=", ")
        level = nextLevel
            
    print("\b\b ]")
    
    
root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 81)
root = insert(root, 1)

print("Inorder 1 ")
inorder(root)

print("\nReverse order 1 ")
inorderReverse(root)
 
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("\nInorder 2 ")
inorder(root)

print("\nReverse order 2 ")
inorderReverse(root)


#printNode(root)

#root = deleteNode(root, 10)

# 
# print("Inorder traversal: ", end=' ')
# 
# 
# print("\nDelete 10")
# 
# print("Inorder traversal: ", end=' ')
# inorder(root)
# =============================================================================
