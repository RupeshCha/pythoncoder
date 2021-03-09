#Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.
#https://leetcode.com/problems/contains-duplicate/
#Input: nums = [1,2,3,1]
#Output: true
from collections import defaultdict
from typing import List
class Solution:
    def containsDuplicate( self, nums:List[int]) -> bool:
        m = defaultdict(int)
        for num in nums:
            if m[num]:
                return True
            m[num] +=1
        return False

nums = [1,2,3,1]
s = Solution()
print(s.containsDuplicate(nums))