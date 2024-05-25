#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        
        for c1, c2 in prerequisites:
            adjList[c2].append(c1)

        visiting = set()

        def hasCycle(crs):
            # no prerequisites
            if adjList[crs] == []:
                return False
            if crs in visiting:
                return True
            
            visiting.add(crs)

            for pre in adjList[crs]:
                if hasCycle(pre):
                    return True
                
            # all nodes connected has no cycle
            visiting.remove(crs)
            adjList[crs] = []
        
        for crs in range(numCourses):
            if hasCycle(crs):
                return False
        return True
        
# @lc code=end

