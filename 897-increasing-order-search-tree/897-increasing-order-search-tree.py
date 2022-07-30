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
        
    def increasingBST_1(self, root, tail = None):
        if not root: return tail
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res
    
    def increasingBST_2(self, root):
        def dfs(node):
            l1, r2 = node, node
            
            if node.left: 
                l1, l2 = dfs(node.left)
                l2.right = node
                
            if node.right:
                r1, r2 = dfs(node.right)
                node.right = r1
            
            node.left = None
            return (l1, r2)
        
        return dfs(root)[0]

            
            