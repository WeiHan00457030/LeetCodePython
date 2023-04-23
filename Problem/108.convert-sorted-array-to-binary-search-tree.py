#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        return self.getNode(nums)
    
    def getNode(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        root = TreeNode(nums[len(nums)//2])
        root.left = self.getNode(nums[0:(len(nums)//2)])
        root.right = self.getNode(nums[(len(nums)//2)+1:len(nums)])
        return root

# @lc code=end

