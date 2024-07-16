# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:34:38 2024

@author: Arjun
"""
class Solution(object):
        
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num = ""
        res = ""
        
        i=0
        while i < len(s):
            if s[i].isdigit():
                num += s[i]
            elif s[i].isalpha():
                res += s[i]
            elif s[i] == '[':
                subStr = self.getString(s[i+1:])
                res += subStr * int(num) if num else subStr
                i += len(subStr) + 1 # +1 for ']' char
                num = ""
            i += 1
        return res
    def getString(self, s):
       str = ""
       num = ""
       for i in range(len(s)):
           if s[i].isalpha():
               str += s[i]
           elif s[i].isdigit():
               num += s[i]
           elif s[i] == '[':
               #str += int(num) * self.getString(s[i+1:]) # check for num
               str += self.getString(s[i+1:])
               num = ""
           elif s[i] == ']':
               return str
       print("Invalid string in getString function ", s)
       return ""                
                
o =Solution()
# =============================================================================
# print("Decoding result is ", o.decodeString("3[a]2[bc]"))     # "aaabcbc"
# print("Decoding result is ", o.decodeString("3[a2[c]]"))      # "accaccacc"
# print("Decoding result is ", o.decodeString("2[abc]3[cd]ef")) #  "abcabccdcdcdef"
# print("Decoding result is ", o.decodeString("abc3[cd]xyz"))   # "abccdcdcdxyz"
# =============================================================================

print("Decoding result is ", o.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")) 
# "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
                

               
            
"""
394. Decode String
Medium
Topics
Companies
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""