#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total / 2

        if target in nums:
            return True
        
        def can_sum(nums,target):
            dp = [False] * (target + 1)
            dp[0] = True

            for num in nums:
                for i in range(target,num-1,-1):
                    if dp[i-num] == True:
                        dp[i] = True
                        if i == target:
                            return True
            return False
        
        

        return can_sum(nums,int(target))
# @lc code=end

