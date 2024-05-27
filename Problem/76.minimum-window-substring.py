#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""
       
        target_dict = {}
        for ch in t:
            if ch in target_dict:
                target_dict[ch] += 1
            else:
                target_dict[ch] = 1
       
        t_cnt = len(t)

        start = 0 
        ans = s
        ans_found = False

        for end,ch in enumerate(s):
            if ch in target_dict:
                if target_dict[ch] > 0:
                    t_cnt -= 1
                target_dict[ch] -= 1

                end += 1

                while t_cnt == 0:
                    ans_found = True
                    tmp = s[start:end]

                    if len(tmp) < len(ans):
                        ans = tmp

                    # push start index
                    ch_start = s[start]

                    if ch_start in target_dict:

                        if target_dict[ch_start] == 0:
                            t_cnt += 1
                        target_dict[ch_start] += 1
                    start += 1

        return ans if ans_found else ""
        
# @lc code=end

