#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
            
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.getDepth(root)
        return self.diameter
    
    def getDepth(self,root):
        if not root:
            return 0
        else:
            lDepth,rDepth = 0,0
            if root.left : 
                lDepth = 1 + self.getDepth(root.left)
            if root.right: 
                rDepth = 1 + self.getDepth(root.right)
            
            if lDepth+rDepth > self.diameter:
                self.diameter = lDepth+rDepth
            return max(lDepth,rDepth)
            
# @lc code=end
