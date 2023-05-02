#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer–Moore majority vote algorithm
        count,sol = 0,None

        for i in nums:
            if count == 0:
                sol = i
            
            if sol == i:
                count += 1
            else:
                count -= 1
        
        return sol
        
# @lc code=end

