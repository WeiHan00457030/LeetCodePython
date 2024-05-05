#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        pos = 0
        sign,value = 0,0

        if len(s) == 0:
            return 0
        
        while pos < len(s):
            char = s[pos]

            if sign == 0:
                if char == "+" or char == "-":
                    sign = 1 if char == "+" else -1
                elif char.isdigit():
                    value = int(char)
                    sign = 1
                elif char != " ":
                    break
            else:
                if char.isdigit():
                    value *= 10
                    value += int(char)
                else:
                    break
            pos += 1
        
        value = sign * value
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)

        return value


# @lc code=end

