#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #return sorted(points,key = lambda x:(x[0]**2 + x[1]**2))[:k]
        h = []
        for i in points:
            dist = i[0]**2 + i[1]**2

            if len(h) < k:
                heapq.heappush(h,(-dist,i[0],i[1]))
            else:
                heapq.heappushpop(h,(-dist,i[0],i[1]))
        
        print(h)


# @lc code=end

