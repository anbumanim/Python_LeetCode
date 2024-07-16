# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 08:59:16 2024

@author: Arjun
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        vws = []
        # Get all the vowels
        for c in s:
            if c in 'AEIOUaeiou':
                vws.append(c)
        
        # Replace vowels in reverse order
        ret = []
        for i,c in enumerate(s):
            if c in 'AEIOUaeiou':
                ret.append(vws.pop())
            else:
                ret.append(c)
        
        st = str(ret)
        
        
        return "".join(ret)
    
    
s = Solution()
print(s.reverseVowels("hello"))



"""
345. Reverse Vowels of a String
Easy
Topics
Companies
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""