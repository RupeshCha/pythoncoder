#Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
#You can return the answer in any order.
#https://leetcode.com/problems/two-sum/
#Input: nums = [2,45,7,11,15], target = 9
#Output: [0,1]
#Output: Because nums[0] + nums[1] == 9, we return [0, 1].
from typing import List

class Solution:
    def twoSum(self,nums:List[int],target:int) -> List[int]:
        seen = {}
        for index,num in enumerate(nums):
            other = target - num
            if other in seen:
                return [seen[other],index]
            else:
                seen[num] = index
        return []
    
nums = [2,45,7,11,15]
target = 9
s = Solution()
print(s.twoSum(nums,target) )