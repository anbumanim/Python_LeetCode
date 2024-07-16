# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 14:42:12 2024

@author: Arjun
"""
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ret = ""
        minLen = min(len(word1), len(word2))

        if minLen == 0 :
            for c,d in zip(word1,word2):
                ret += c + d
            return ret
        # iterate less len and merge
        for i in range(minLen):
            ret += word1[i] + word2[i]

        # slice lengthy at the end
        if len(word1) > len(word2):
            ret += word1[minLen:]
        elif len(word2) > len(word1):
            ret += word2[minLen:]

        return ret
        
print(Solution().mergeAlternately("cdf", "a"))

# Simple solution
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a, b = len(word1), len(word2)
        ans = ""
        for i in range(min(a, b)):
            ans += word1[i]
            ans += word2[i]
        if a > b:
            ans += word1[b:]
        else:
            ans += word2[a:]
        return ans 



"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
"""


"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a, b = len(word1), len(word2)
        ans = ""
        for i in range(min(a, b)):
            ans += word1[i]
            ans += word2[i]
        if a > b:
            ans += word1[b:]
        else:
            ans += word2[a:]
        return ans 
"""
