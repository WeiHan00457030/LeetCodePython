#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # sorted_p = sorted(p)
        # ans = []
        # ans_now = False

        # for i in range(len(s)-len(p)+1):
        #     s_i = s[i:i+len(p)]
            
        #     if ans_now:
        #         if s_i[-1] == s[i-1]:
        #             ans.append(i)
        #         else:
        #             ans_now = False
        #     elif sorted(s_i) == sorted_p:
        #         ans.append(i)
        #         ans_now = True

        # return ans

        ans = []
        pArray, sArray = [0] * 26, [0] * 26
        for c in p:
            pArray[ord(c)-ord('a')] += 1
        init = s[:len(p)]
        for c in init:
            sArray[ord(c)-ord('a')] += 1

        # compare index 0
        if pArray == sArray:
            ans.append(0)

        for i in range(1,len(s)-len(p)+1):
            sArray[ord(s[i-1])-ord('a')] -= 1 # remove previous
            sArray[ord(s[i+len(p)-1])-ord('a')] += 1 # append now
            if pArray == sArray:
                ans.append(i)

        return ans
# @lc code=end

