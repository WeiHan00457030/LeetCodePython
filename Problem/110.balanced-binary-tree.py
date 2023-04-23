#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return True if self.getDepth(root) > 0 else False
    
    def getDepth(self,root:Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        dLeft  = self.getDepth(root.left)
        dRight = self.getDepth(root.right)

        # not balance
        if dLeft < 0 or dRight < 0 or abs(dLeft-dRight) > 1:
            return -1
        else:
            return max(dLeft,dRight)+1

        
# @lc code=end

