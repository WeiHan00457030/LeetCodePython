#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        previous = []
        ans = []
        intervals.sort(key = lambda x:x[0])
        for interval in intervals:
            if not previous:
                previous = interval
                continue

            if previous[1] >= interval[0]:
                if previous[1] <= interval[1]:
                    previous = [previous[0]] + [interval[1]]
            else:
                ans.append(previous)
                previous = interval
        
        ans.append(previous)
        return ans
# @lc code=end

