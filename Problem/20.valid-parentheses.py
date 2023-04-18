#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            match s[i]:
                case '('|'['|'{':
                    stack.append(s[i])
                case ')':
                    if (len(stack) == 0 or stack[len(stack)-1] != '('):
                        return False
                    else:
                        stack.pop()
                case ']':
                     if (len(stack) == 0 or stack[len(stack)-1] != '['):
                         return False
                     else:
                        stack.pop()
                case '}':
                     if (len(stack) == 0 or stack[len(stack)-1] != '{'):
                         return False
                     else:
                        stack.pop()

        if (len(stack)>0):
            return False
        else:
            return True
# @lc code=end

