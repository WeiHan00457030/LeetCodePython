#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l,r = 0,len(height)-1
        
        while l < r:
            capacity = min(height[l],height[r]) * (r-l)
            res = max(res,capacity)

            if height[l] < height[r]:
                l += 1
            elif height[l] >= height[r]:
                r -= 1

        return res
        
        
# @lc code=end

