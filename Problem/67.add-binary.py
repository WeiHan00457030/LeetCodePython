#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = list(map(int,str(int(a) + int(b))))
        carry = 0
        for i in reversed(range(len(sum))):
            if sum[i] + carry >= 2:
                sum[i] = sum[i] + carry - 2
                carry = 1
            else:
                sum[i] = sum[i] + carry
                carry = 0
            
            if not i and carry:
                sum.insert(0,1)
            
        return "".join(map(str,sum))

        
    
# @lc code=end

