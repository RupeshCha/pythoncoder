#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]
from typing import List
class Solution:
    def moveZeros(self,nums:List[int]) -> List[int]:
        j= 0
        for num in nums:
            if num != 0 :
                nums[j] = num
                j += 1
        for x in range(j,len(nums)):
            nums[x] = 0
        return nums    

s = Solution()
print(s.moveZeros([0,1,0,3,12]))
