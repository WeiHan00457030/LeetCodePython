#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.cloneNode(node,{})

    def cloneNode(self, node, visited):
        if not node: return None

        newNode = Node(node.val)
        visited[node.val] = newNode

        for neighbor in node.neighbors:
            if neighbor.val not in visited:
                newNode.neighbors.append(self.cloneNode(neighbor,visited))
            else:
                newNode.neighbors.append(visited[neighbor.val])
        
        return newNode
# @lc code=end

