#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        length = len(word1) if len(word1) < len(word2) else len(word2)
        
        ans = ""
        for i in range(length):
            ans += word1[i] + word2[i]
        
        ans += word1[length:] + word2[length:]
        return ans
# @lc code=end

