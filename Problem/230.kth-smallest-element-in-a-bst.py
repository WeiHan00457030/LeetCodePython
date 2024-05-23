#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            
            if len(res) == k:
                return
            res.append(root.val)
            
            inorder(root.right)

            return
        
        inorder(root)
        
        return res[-1]
    

# @lc code=end

