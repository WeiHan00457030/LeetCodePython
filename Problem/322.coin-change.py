#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max = amount + 1

        dp = [max] * max
        dp[0] = 0

        for i in range(1,max):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i],dp[i-coin]+1)

        return -1 if dp[amount] > amount else dp[amount]


# @lc code=end

