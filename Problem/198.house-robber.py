#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_0 = 0
        dp_1 = nums[0]
        for i in nums[1:]:
            dp = max(dp_0 + i, dp_1)
            dp_0 = dp_1
            dp_1 = dp
        return dp_1
# @lc code=end

