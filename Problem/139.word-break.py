#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def build_dp(cur:str, dp = {}):
            if cur in dp:
                return dp[cur]
            
            if not cur:
                return True
            
            for word in wordDict:
                if cur.startswith(word):
                    newCur = cur[len(word):]
                    if build_dp(newCur,dp):
                        dp[cur] = True
                        return True
            dp[cur] = False
        
        return build_dp(s)
# @lc code=end

