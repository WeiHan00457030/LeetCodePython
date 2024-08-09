#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # build graph & Calculate the in-degree of each node
        gh = defaultdict()
        in_degree = [0] * numCourses

        for course,preq in prerequisites:
            gh[preq].append(course)
            in_degree[course] += 1
        
        # Start Topological sort
        # 1.Find the start nodes (nodes without in-degree)
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        result = []
        # 2. search neighbors from start node and delete its in-degree
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in gh[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        # check cycle
        if len(result) < numCourses:
            return []

        return result

        

# @lc code=end

