#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ans = []

        for i in intervals:
            if i[1] < newInterval[0]:
                ans.append(i)
            # newInterval start in range of interval
            elif i[0] > newInterval[1]:
                ans.append(newInterval)
                newInterval = i
            else:
                newInterval[0] = min(i[0],newInterval[0])
                newInterval[1] = max(i[1],newInterval[1])
            
        ans.append(newInterval)
        
        return ans
                
# @lc code=end

