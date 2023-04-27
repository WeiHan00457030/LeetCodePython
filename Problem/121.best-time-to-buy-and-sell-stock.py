#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0
        buy = prices[0]
        for i in range(len(prices)-1):
            buy = min(buy,prices[i])
            if prices[i+1] - buy > maxProfit:
                maxProfit = prices[i+1] - buy
        return maxProfit
# @lc code=end

