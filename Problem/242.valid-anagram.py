#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
            
        return True
# @lc code=end

