#https://leetcode.com/problems/trapping-rain-water/
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        
        # initialze two points that one at the start of the height array
        # while the other one at the end of height array
        left 0
        right = len(height) - 1
        
        water, max_height_left, max_height_right = 0, 0, 0
        
        while left < right:
            if height[left] <= height[right]:
                max_height_left = max(max_height_left, height[left])
                water += max_height_left - height[left]
                left += 1
            else:
                max_height_right = max(max_height_right, height[right])
                water += max_height_right - height[right]
                right -= 1
        
        return water