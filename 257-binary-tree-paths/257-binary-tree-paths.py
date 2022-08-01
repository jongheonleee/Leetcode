# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = [] 
        
        def dfs(root, tmp):
            if root is None:
                return
            
            tmp += str(root.val) + '->'
            
            if not root.left and not root.right:
                res.append(tmp)
                return
            
            if root.left:
                dfs(root.left, tmp)
            
            if root.right:
                dfs(root.right, tmp)
                
        dfs(root, '')
        
        for i in range(len(res)):
            res[i] = res[i][:-2]
            
        return res
        
        