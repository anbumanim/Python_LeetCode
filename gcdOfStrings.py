# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:19:33 2024

@author: Arjun
"""

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1 = len(str1)
        len2 = len(str2)
        
        if len1 == len2:
            return str1 if str2 == str1 else ""
                
        if len1 > len2:
            if len1 % len2 == 0 and str1 == str2 * (len1 // len2):
                return str2
            else:
                return ""
        else:
            if len2 % len1 == 0 and str2 == str1 * (len2 // len1):
                return str1
            else:
                return ""

print(Solution().gcdOfStrings("ABABAB", "AB"))
"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""