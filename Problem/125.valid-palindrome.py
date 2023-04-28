#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum,s))
        s = s.lower()
        if not s:
            return True
        elif s == s[::-1]:
            return True
        else:
            return False
# @lc code=end

