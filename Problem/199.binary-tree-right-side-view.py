#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        
        queue = []
        queue.append(root)
        ans = []

        while queue:
            ans.append(queue[-1].val)

            for i in range(len(queue)):
                ele = queue.pop(0)
                
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)


        return ans

# @lc code=end

