#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        appear = set()
        palindrome = 0
        for i in s:
            if i in appear:
                appear.remove(i)
                palindrome += 2
            else:
                appear.add(i)
        
        return palindrome + 1 if appear else palindrome
            
# @lc code=end

