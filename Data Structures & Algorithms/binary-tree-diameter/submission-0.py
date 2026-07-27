# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftheight=self.maxheight(root.left)
        rightheight=self.maxheight(root.right)
        dia=leftheight+rightheight
        subd=max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        dia=max(dia,subd)
        return dia

    def maxheight(self,root: Optional[TreeNode]):
        if not root:
            return 0
        return 1+max(self.maxheight(root.left),self.maxheight(root.right))