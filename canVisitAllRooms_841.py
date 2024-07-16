# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 10:42:03 2024

@author: Arjun
"""
class Solution:
    def canVisitAllRooms(self, rooms): # List[List[int]]) -> bool:
        visited_rooms = set()
        stack = [0] # for rooms that we need to visit and we start from room [0]
        
        while stack: 
            #if len(visited_rooms) == len(rooms) :
            #    return True
            room = stack.pop() 
            visited_rooms.add(room)
            for key in rooms[room]:
                if key not in visited_rooms:
                    stack.append(key)
        return len(visited_rooms) == len(rooms)      

#    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#        if len(rooms[0])==0:
#            return False
#        v={0:1}
#        l=[]
#        l.extend(rooms[0])
#        while l:
#            m=l.pop(0)
#            if m not in v:
#                v[m]=1
#                l.extend(rooms[m])
#        if len(v)==len(rooms):
#            return True
#        return False

#    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#        # create isVisited with default False
#        isVisited = [False for _ in range(len(rooms))]
#        isUnlocked = [False for _ in range(len(rooms))]
#        isUnlocked[0] = True
#        
#        # visit each non visited room
#        r = 0
#        visitedCount = 0
#        while(visitedCount < len(rooms)):
#            # unlock the rooms with key
#            for k in rooms[r]:
#                isUnlocked[k] = True
#                
#            isVisited[r] = True
#            visitedCount += 1
#            
#            # next room
#            # find rooms unlocked and not visited
#            r = -1
#            for i in range(len(rooms)):
#                if not isVisited[i] and isUnlocked[i]:
#                    r=i
#                    break
#            
#            if r == -1 and visitedCount < len(rooms):
#                return False
#        return True
    
o = Solution()
print("can visited all rooms ", o.canVisitAllRooms([[1],[2],[3],[]]))
print("can visited all rooms ", o.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))

"""
841. Keys and Rooms
Medium
Topics
Companies
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

 

Example 1:

Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.
Example 2:

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.
 

Constraints:

n == rooms.length
2 <= n <= 1000
0 <= rooms[i].length <= 1000
1 <= sum(rooms[i].length) <= 3000
0 <= rooms[i][j] < n
All the values of rooms[i] are unique.
"""