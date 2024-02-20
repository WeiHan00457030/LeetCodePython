#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        
        i,j = 0,0
        output = 0
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                j += 1
                i += 1
                output += 1
            elif s[j] < g[i]:
                j += 1
        
        return output
# @lc code=end

