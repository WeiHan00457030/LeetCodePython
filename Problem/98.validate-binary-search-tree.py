#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    last = None
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root != None:
            if not self.isValidBST(root.left): return False
            
            if self.last == None or self.last < root.val:
                self.last = root.val
            else:
                return False
            
            if not self.isValidBST(root.right): return False
        
        return True
        
# @lc code=end

