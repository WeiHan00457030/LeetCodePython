#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        dict = {
            "2":"abc","3":"def","4":"ghi",
            "5":"jkl","6":"mno","7":"pqrs",
            "8":"tuv","9":"wxyz"
        }

        res = []
        def construct(idx, str):
            print(idx,str)
            if idx == len(digits):
                res.append(str)
                return
            
            for letter in dict[digits[idx]]:
                construct(idx+1, str+letter)

        construct(0,"")

        return res

# @lc code=end

