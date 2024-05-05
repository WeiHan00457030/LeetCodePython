#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1] * len(nums)

        pre,pos = 1,1
        # pre = nums[0]*.....nums[i]
        # pos = nums[-1] *.....nums[i]
        
        for i in range(len(nums)):
            ans[i] *= pre
            ans[len(nums) -i+1] *= pos

            pre *= nums[i]
            pos *= nums[len(nums)-i+1]
# @lc code=end

