#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for i in strs:
            while (i.find(ans) != 0 and len(ans) > 0):
                ans = ans[0:len(ans)-1]
        return ans
# @lc code=end

#存tmp