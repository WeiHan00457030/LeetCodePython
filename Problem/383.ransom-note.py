#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            index = magazine.find(i)
            if index == -1:
                return False
            else:
                magazine = magazine[0:index] + magazine[index+1:len(magazine)]
        return True
# @lc code=end

