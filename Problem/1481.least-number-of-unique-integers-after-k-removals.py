#
# @lc app=leetcode id=1481 lang=python3
#
# [1481] Least Number of Unique Integers after K Removals
#

# @lc code=start
import collections
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arr = list(collections.Counter(arr).values())
        arr.sort()
        for i in range(len(arr)):
            if k >= arr[i]:
                k -= arr[i]
            else:
                return len(arr) - i
            
            if k == 0:
                return len(arr) -i -1
        
# @lc code=end

