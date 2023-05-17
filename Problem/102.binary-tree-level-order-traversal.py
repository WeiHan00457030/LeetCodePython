#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = []
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        self.ans = []
        self.getNode([root])
        return self.ans
    
    def getNode(self,nodeList):
        tmp = []
        nextList = []
        for i in nodeList:
            tmp.append(i.val)
            if i.left != None:
                nextList.append(i.left)
            if i.right != None:
                nextList.append(i.right)

        self.ans.append(tmp)
        
        if len(nextList) > 0:
            self.getNode(nextList)
        
# @lc code=end

