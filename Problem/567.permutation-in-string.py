#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        arr = [0] * 26

        for ch in s1:
            arr[ord(ch) - ord('a')] += 1

        collected = [0]*26

        for index in range(len(s2)):
            collected[ord(s2[index]) - ord('a')] += 1

            if index > len(s1)-1:
                start_ch = s2[index-len(s1)]
                collected[ord(start_ch) - ord('a')] -= 1

            if collected == arr:
                return True
        return False


        
        
# @lc code=end

