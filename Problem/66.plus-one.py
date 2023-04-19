#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in reversed(range(len(digits))):
            ### plus one
            if i == len(digits) - 1:
                digits[i] += 1

            ### carry
            if digits[i] + carry == 10:
                carry = 1
                digits[i] = 0
            else:
                digits[i] += carry
                carry = 0
            ### last digit's carry
            if not i and carry:
                digits.insert(0,carry)
        return digits
# @lc code=end

