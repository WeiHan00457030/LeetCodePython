#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left,right = 1,x
        while left <= right:
            mid= (left + right) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 > x:
                right = mid - 1
            else:
                left = mid + 1
        return right
# @lc code=end

