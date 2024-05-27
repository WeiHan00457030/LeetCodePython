#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # last seen index
        dict = {}
        
        start = 0
        ans = 0
        for end in range(len(s)):

            if s[end] not in dict:
                ans = max(ans,end-start+1)
            else:
                ans = max(ans,end-start)
                new_start = dict[s[end]] + 1
                
                # remove seen before new_start
                for ch in s[start:new_start-1]:
                    del dict[ch]

                start = new_start
                
            dict[s[end]] = end    
    
        
        return ans
# @lc code=end

