#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root : return 0

        lDepth = self.minDepth(root.left)
        rDepth = self.minDepth(root.right)

        if not root.left and not root.right:
            return 1
        elif not root.left:
            return 1 + rDepth
        elif not root.right:
            return 1 + lDepth

        return min(lDepth,rDepth)+1
# @lc code=end

