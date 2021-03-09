#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.
#Input: nums = [3,2,3]
#Output: 3
#Input: nums = [2,2,1,1,1,2,2]
#Output: 2

from typing import List
class Solution:
    def majorityElement(self,nums:List[int]) -> int:
        m = {}
        for num in nums:
            m[num] = m.get(num,0) + 1
        for num in nums:
            if m[num] > (lem(nums)//2):
                return num

class Solution1:
    def majorityElement1(self, nums):
        nums.sort()
        return nums[len(nums)//2]

nums = [2,2,1,1,1,2,2]
s = Solution()
print(s.majorityElement(nums))