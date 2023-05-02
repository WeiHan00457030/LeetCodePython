#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start,end = 1,n
        
        while start < end:
            pivot = (start+end) // 2

            if isBadVersion(pivot):
                end = pivot
            else:
                start = pivot +1
        
        return start
# @lc code=end

