# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:46:16 2024

@author: Arjun
"""
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #grid.transpose()
        trans = []
        
        for c in range(len(grid)):
            colList = []
            for r in range(len(grid)):
                colList.append(grid[r][c])
            trans.append(colList)
        
        count = 0
        
        for r in range(len(grid)):
            for c in range(len(grid)):
                if(grid[r] == trans[c]):
                    count += 1
                    
        return count
        
        
o = Solution()
print("No of equal pairs is ", o.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print("No of equal pairs is ", o.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))


"""
2352. Equal Row and Column Pairs
Medium
Topics
Companies
Hint
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
"""