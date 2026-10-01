# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        bal = True
        def dfs(node):
            nonlocal bal
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left>right+1 or left+1<right:
                bal = False
                return bal
            
            return 1+max(left, right)
        dfs(root)
        return bal
