#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        
        res = []
        open,close = 0,0
        for i,c in enumerate(s):
            res.append(c)

            if c == '(':
                open += 1
            elif c == ')':
                if open == close:
                    res.pop()
                else:
                    close += 1

        remove_open = open - close
        index = len(res)-1

        while index >=0 and remove_open > 0:
            if res[index] == '(':
                res[index] = ''
                remove_open -=1
            index -= 1

        return ''.join(res)

# @lc code=end

