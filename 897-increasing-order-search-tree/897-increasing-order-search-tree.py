# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy_node = TreeNode(-1)
        res = []
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            
        dfs(root)
        crnt_node = dummy_node
        for val in res:
            node = TreeNode(val)
            crnt_node.right = node
            crnt_node = crnt_node.right
            
        return dummy_node.right
        

            
            