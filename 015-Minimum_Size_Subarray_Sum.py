#Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a contiguous subarray [numsl, numsl+1, ..., 
# numsr-1, numsr] of which the sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.
#https://leetcode.com/problems/minimum-size-subarray-sum/
#input: target = 7, nums = [2,3,1,2,4,3]
#Output: 2
#Explanation: The subarray [4,3] has the minimal length under the problem constraint.


from typing import List

class Solution:
    def twoSum(self,nums:List[int],target:int) -> List[int]:
    
        for index,num in enumerate(nums):
            if ( index <=  len(nums) - 1 - 1):
                temp = num + nums[index + 1]
                if (temp == target):
                    return [num,nums[index + 1]]

           
        return []
    
nums = [2,3,1,2,4,3]
target = 7
s = Solution()
print(s.twoSum(nums,target) )