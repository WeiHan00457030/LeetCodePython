#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = self.buildAdjacencyList(numCourses, prerequisites)
        state = [0] * numCourses
        def hasCycle(v):
            if state[v] == 1:
                # This vertex is processed so we pass.
                return False
            if state[v] == -1:
                # This vertex is being processed and it means we have a cycle.
                return True
    
            # Set state to -1
            state[v] = -1
    
            for i in adjList[v]:
                if hasCycle(i):
                    return True
    
            state[v] = 1
            return False
    
        # we traverse each vertex using DFS, if we find a cycle, stop and return
        for v in range(numCourses):
            if hasCycle(v):
                return False
    
        return True
        
    def buildAdjacencyList(self, n, edgesList):
        adjList = [[] for _ in range(n)]
        # c2 (course 2) is a prerequisite of c1 (course 1)
        # i.e c2c1 is a directed edge in the graph
        for c1, c2 in edgesList:
            adjList[c2].append(c1)
        return adjList
# @lc code=end

