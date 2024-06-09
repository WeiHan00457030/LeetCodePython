#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        start = 0
        while start < len(gas):

            loop_gas = gas[start:] + gas[:start]
            loop_cost = cost[start:] + cost[:start]
            count = 0 # if start from a ans stuck at b, then start from b in next iteration
            tank = 0

            for i in range(len(loop_gas)):
                tank = tank+loop_gas[i]-loop_cost[i]
                count += 1
                
                if tank < 0:
                    break

            if tank >= 0 :
                return start
            else:
                start = start + count
        
        return -1
            
                
# @lc code=end

