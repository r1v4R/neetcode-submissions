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
        lh,rh=0,0
        st=[root]
        while st:
            node=st.pop()
            lh,rh=0,0
            if node.left:
                st.append(node.left)
                lh=self.calcH(node.left)
            if node.right:
                st.append(node.right)
                rh=self.calcH(node.right)
            if (abs(rh-lh)>1):
                print("node is",node.val,"rh is ",rh,"and lh is",lh )
                return False
        return True

    def calcH(self,root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return(1+max(self.calcH(root.left),self.calcH(root.right)))        