#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        queue = deque([(root,0)])
        max_width = 0

        while queue:
            _,head = queue[0]
            for i in range(len(queue)):
                node,index = queue.popleft()
                ## add node
                if node.left:
                    queue.append([node.left,2*index])
                if node.right:
                    queue.append([node.right,2*index+1])
                
            ##cal max
            max_width = max(max_width,index - head + 1)
            
        return max_width
# @lc code=end

