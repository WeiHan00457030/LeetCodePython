#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dpList = [None] * (amount+1)
        dpList[0] = 0
        coins = sorted(coins)[::-1]
        
        # dp from 0 to amout
        for i in range(1,amount+1):
            for coin in coins:
                # if i - coin has solution, [i] = [i-coin] + 1
                if i >= coin and dpList[i-coin] != None:
                    
                    if dpList[i] == None:
                        dpList[i] = dpList[i-coin]+1
                    else:
                        dpList[i] = min(dpList[i],dpList[i-coin] + 1)
                    
        
        #print(dpList)
        return dpList[amount] if (dpList[amount] != None) else -1


        

# @lc code=end

