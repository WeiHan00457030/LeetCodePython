#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) <= 1:
            return s
        
        def expend(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-= 1
                r+=1 
            return s[l+1:r]
        
        lognest_palindrome = ""

        for i in range(len(s)-1):
            a = expend(i,i)
            b = expend(i,i+1)

            if len(a) > len(lognest_palindrome):
                lognest_palindrome = a
            if len(b) > len(lognest_palindrome):
                lognest_palindrome = b
        
        return lognest_palindrome

# @lc code=end

