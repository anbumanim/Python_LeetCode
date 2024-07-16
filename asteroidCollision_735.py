# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:33:34 2024

@author: Arjun
"""
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        res = []

        for a in asteroids:

            while res and a < 0 < res[-1]:
                if -a > res[-1]:
                    res.pop()
                    continue
                elif -a == res[-1]:
                    res.pop()
                break
            else:
                res.append(a)

        return res
        


o = Solution()
print("After collision ", o.asteroidCollision([5,10,-5]))
print("After collision ", o.asteroidCollision([8,-8]))
print("After collision ", o.asteroidCollision([10,2,-5]))
print("After collision ", o.asteroidCollision([1,2,3,4,-5]))
print("After collision ", o.asteroidCollision([-2,-1,1,2]))
print("After collision ", o.asteroidCollision([-2,-2,1,-2, -3]))
print("After collision ", o.asteroidCollision([-2,2,1,-2]))
print("After collision ", o.asteroidCollision([1,-2,-2,-2]))



"""
735. Asteroid Collision
Medium
Topics
Companies
Hint
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0

my solution:
============
        a = asteroids
        res = [a[0]]
        Forward = a[0] >= 0 

        for i in range(1, len(a)):
            if not Forward: # reverse direction
                res.append(a[i])
                Forward = a[i] >= 0
            else: # forward direction
                if a[i] >= 0:   # [1,2,3,4], 3
                    res.append(a[i])
                    Forward = True
                else:
                    if a[i] + res[-1] == 0:  # [-3,4] -4
                        res.pop()
                        Forward = res and res[-1] >= 0
                    else:  # [1,2,3,4] -5 or -3
                        for x in range(len(res)-1, -1, -1):
                            if not Forward:  # [-3] -4
                                res.append(a[i])
                                Forward = a[i] >= 0
                                break
                            if a[i] + res[-1] < 0:  # [-3,4] -5
                                res.pop()
                                if not res:
                                    res.append(a[i])
                                    Forward = res[-1] >= 0
                                    break
                                else:
                                    Forward = res[-1] >= 0
                                
                            elif a[i] + res[-1] == 0:  # [-3,4] -4
                                res.pop()
                                Forward = res and res[-1] >= 0
                                break
                            else: # [1,2,3,4] -3
                                break
            
            print(res, a[i])
        return res


old version:
============
        a = asteroids
        res = [asteroids[0]]
        k = 0
        
        i = 1
        #for i in range(1, len(a)):
        while i < len(a):
            if res[k] >= 0 and a[i] >= 0 or  res[k] < 0 and a[i] < 0:
                res.append(a[i])
                k += 1
            else:
                if res[k] >= 0 and res[k] == abs(a[i]):   # same value in opposite direction
                    res.pop()
                    k -= 1
                elif res[k] >= 0 and res[k] > abs(a[i]):   # new value is weaker, leave it
                    #i += 1
                    #continue
                    None
                elif res[k] < 0 and a[i] > 0:   # left -ve right +ve, add it
                    res.append(a[i])
                    k += 1
                else: # new value is stronger and -ve
                    res.pop()
                    #res.append(a[i])
                    k -= 1
                    #i -= 1
            
            print(res, a[i])
            i += 1
        return res




"""