# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(root):
            nonlocal ans
            if not root:
                return

            
            dfs(root.left)
            ans += 1
            dfs(root.right)
            
        dfs(root)
        return ans
            