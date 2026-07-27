# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        st=[[root,1]]
        maxd=0
        while st:
            node,depth=st.pop()
            if node:
                maxd=max(maxd,depth)
                st.append([node.left,depth+1])
                st.append([node.right,depth+1])
        return maxd

        