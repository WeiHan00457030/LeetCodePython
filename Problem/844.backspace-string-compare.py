#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sString,tString = "",""

        for i in s:
            if i != '#':
                sString += i
            else:
                sString = sString[0:len(sString)-1]
        
        for i in t:
            if i != '#':
                tString += i
            else:
                tString = tString[0:len(tString)-1]

        return sString == tString
# @lc code=end

