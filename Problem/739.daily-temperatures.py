#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] # store index of days that didn't find warmer day
       
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
           
            for j in stack[::-1]: #the tmp in stack would be large to small
                if temperatures[i] > temperatures[j]:
                    ans[j] = i-j
                    stack.pop()
                else:
                    break
            stack.append(i)
        
        return ans
# @lc code=end

