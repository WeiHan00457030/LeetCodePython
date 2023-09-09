#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def construct(current,wordDict, dp={}):
            if current in dp:
                return dp[current]
            
            if not current:
                return True
            
            for word in wordDict:
                if current.startswith(word):
                    newCur = current[len(word):]
                    
                    if construct(newCur,wordDict,dp):
                        dp[current] = True
                        return True
            dp[current] = False
            return False

        return construct(s,wordDict)
# @lc code=end

