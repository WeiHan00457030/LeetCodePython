#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums) # store max length in i
        max = 1

        for i in range(len(nums)):
            tmp = 1
            for j in range(i): # compare with 0~(i-1)
                if nums[j] < nums[i] and dp[j]+1 > tmp:
                    tmp = dp[j]+1
                
                dp[i] = tmp
                if tmp > max:
                    max = tmp
        return max
# @lc code=end

