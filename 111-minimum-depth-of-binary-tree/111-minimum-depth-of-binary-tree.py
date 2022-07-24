# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        cand = []
        
        def dfs(node, cnt) -> None:
            if node:
                dfs(node.left, cnt + 1)
                dfs(node.right, cnt + 1)
                
            if node and node.left is None and node.right is None:
                cand.append(cnt)
                
                
        dfs(root, 1)
        return min(cand) if cand else 0
        
        
        