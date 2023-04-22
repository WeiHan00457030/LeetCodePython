#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        i_1 = 0; i_2 = 1; tmp = 0
        for i in range(n):
            tmp = i_1 + i_2
            i_1 = i_2
            i_2 = tmp
        
        return i_2
# @lc code=end

