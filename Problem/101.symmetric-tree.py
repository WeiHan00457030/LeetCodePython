#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        tLeft = root.left
        tRight = root.right

        return self.sameTree(tLeft,tRight)

    def sameTree(self,tLeft:Optional[TreeNode], tRight: Optional[TreeNode]) -> bool:
        if not tLeft and not tRight:
            return True
        elif not tLeft or not tRight:
            return False
        
        if tLeft.val != tRight.val:
            return False
        
        return self.sameTree(tLeft.left,tRight.right) and self.sameTree(tLeft.right,tRight.left)
# @lc code=end

