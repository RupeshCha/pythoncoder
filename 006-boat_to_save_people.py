#You are given an array people where people[i] is the weight of the ith person, 
#and an infinite number of boats where each boat can carry a maximum weight of limit. 
#Each boat carries at most two people at the same time, 
#provided the sum of the weight of those people is at most limit.
#Return the minimum number of boats to carry every given person.
#https://leetcode.com/problems/boats-to-save-people/
#Input: people = [3,2,2,1], limit = 3
#Output: 3
#Explanation: 3 boats (1, 2), (2) and (3)
from typing import List
class Solution:
    def numberOfBoat(self,people:List[int],Limit:int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boat = 0

        while ( left <= right):

            if (left == right):
                boat += 1
                break

            if ( (people[left] + people[right]) <= limit ):
                left += 1

            right -= 1
            boat += 1
        return boat
    
s = Solution()
people = [3,2,2,1]
limit = 3

print(s.numberOfBoat(people,limit))
