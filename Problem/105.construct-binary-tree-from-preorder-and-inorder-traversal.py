#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # pre: root->left->right
        # in:  left->root->right
        


        def buildTree(preorder,inorder):
            
            if not preorder or not inorder:
                return None
            
            #print("pre",preorder)
           # print("in",inorder)
            if not preorder:
                return None
            
            root_val = preorder[0]

            if root_val in inorder:
                inorder_index = inorder.index(root_val)
                root = TreeNode(preorder.pop(0))
                #print("left")
                root.left = buildTree(preorder,inorder[:inorder_index])
                #print("right")
                root.right = buildTree(preorder,inorder[inorder_index+1:])
            
            return root

        return buildTree(preorder,inorder)
# @lc code=end

