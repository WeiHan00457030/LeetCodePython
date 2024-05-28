#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_len,max_count = 0,0
        arr = collections.Counter()

        for idx in range(len(s)):
            arr[s[idx]] += 1

            max_count = max(arr[s[idx]],max_count)

            if (k+max_count) > max_len:
                max_len += 1
            else:
                arr[s[idx-max_len]] -= 1
            
        return max_len
        
# @lc code=end

