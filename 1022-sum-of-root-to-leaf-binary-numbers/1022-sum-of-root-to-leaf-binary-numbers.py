# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, crnt_num):
            nonlocal root_to_leaf
            if root:
                crnt_num = (crnt_num << 1) | root.val
                print(crnt_num)
                
                if not (root.left or root.right):
                    root_to_leaf += crnt_num

                dfs(root.left, crnt_num)
                dfs(root.right, crnt_num)
                
        root_to_leaf = 0
        dfs(root, 0)
        return root_to_leaf
        