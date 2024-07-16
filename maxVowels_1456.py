# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:59:11 2024

@author: Arjun
"""

class Solution(object):
    def maxVowels(self, s, k) -> int:
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        curK = 0
        maxK = 0
        vowels = "aeiou"
        
        for c in s[:k]:
            if c in vowels:
                curK += 1
        if curK == k:
            return k
        
        maxK = curK
        
        for end in range(k, len(s)):
            if s[end-k] in vowels:
                curK -= 1
            if s[end] in vowels:
                curK += 1
            if curK > maxK:
                maxK = curK
            if maxK == k:
                return k

        return maxK
            
o = Solution()

#print("Max = ", o.maxVowels("abciiidef", 4))
print("Max = ", o.maxVowels("leetcode", 3))
"""
1456. Maximum Number of Vowels in a Substring of Given Length
Medium
Topics
Companies
Hint
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
"""