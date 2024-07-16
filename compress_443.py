# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 13:42:26 2024

@author: Arjun
"""

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        ch = chars[0]  # current charactor to compress
        cursor = 1     # index where to start writing the output list
        count = 1      # count of current compression
        
        for i in range(1, len(chars)):
            # increment count on same charactor
            if chars[i] == ch:
                count += 1
            else:
                if count == 1:
                    ch = chars[i]
                    chars[cursor] = ch
                    cursor += 1
                    count = 1
                else:
                    countStr = list(str(count))
                    for c in range(len(countStr)):
                        chars[cursor + c] = countStr[c]
                    
                    cursor += len(countStr)
                    ch = chars[i]
                    chars[cursor] = ch
                    cursor += 1
                    count = 1
                    
        # end of the loop
        # if count == 1 delete the remaining list elements
        if count == 1:
            del chars[cursor:]
        else:
            countStr = list(str(count))
            for c in range(len(countStr)):
                chars[cursor + c] = countStr[c]
            cursor += len(countStr)
            del chars[cursor:]
            
        print("Result is " + " ".join(chars))
        return len(chars)
        
o = Solution()  
#print(o.compress(["a","a","b","b","c","c","c"]))
print(o.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
"""

443. String Compression
Medium
Topics
Companies
Hint
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.



old code:
=========
        for i in range(1, len(chars)):
            # increment count on same charactor
            if chars[i] == ch:
                count += 1
            else:
                # check count < 10
                if count == 1:
                    ch = chars[i]
                    chars[cursor] = ch
                    cursor += 1
                    count = 1
                elif count < 10:
                    chars[cursor] = str(count)
                    ch = chars[i]
                    chars[cursor+1] = ch
                    cursor += 2
                    count = 1
                elif count < 100:
                    chars[cursor] = str(count // 10)
                    chars[cursor+1] = str(count % 10)
                    ch = chars[i]
                    chars[cursor+2] = ch
                    cursor += 3
                    count = 1
                elif count < 1000:
                    chars[cursor] = str(count // 100)
                    chars[cursor+1] = str((count % 100) // 10)
                    chars[cursor+2] = str(count % 10)
                    ch = chars[i]
                    chars[cursor+3] = ch
                    cursor += 4
                    count = 1
                #elif count < 10000:
                else:
                    chars[cursor] = str(count // 1000)
                    chars[cursor+1] = str((count % 1000) // 100)
                    chars[cursor+2] = str((count % 100) // 10)
                    chars[cursor+3] = str(count % 10)
                    ch = chars[i]
                    chars[cursor+4] = ch
                    cursor += 5
                    count = 1
                    
        # end of the loop



"""