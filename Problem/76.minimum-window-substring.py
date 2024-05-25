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
        
        target_dict = collections.defaultdict(int)
        for ch in t:
            target_dict[ch] += 1
        
        start,end = 0,0
        t_cnt = len(t)

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
                    
                    if len(tmp) <= len(ans):
                        ans = tmp
                    # pust start index
                    if s[start] in target_dict:
                        if target_dict[s[start]] == 0:
                            t_cnt += 1

                        target_dict[s[start]] += 1

                    start += 1

        return ans if ans_found else ""    
# @lc code=end

