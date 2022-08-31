# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deepest_leaves = collections.defaultdict(list)
        max_level = -1
        
        def dfs(root, crnt_level):
            if root is None:
                return
            
            deepest_leaves[crnt_level] += [root.val]
            
            dfs(root.left, crnt_level+1)
            dfs(root.right, crnt_level+1)
            
        dfs(root, 0)
            
        for key, values in deepest_leaves.items():
            print(key, values)
            
        return sum(values)
        
            
            
            
        