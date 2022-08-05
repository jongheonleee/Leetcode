# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def dfs(root): 
            if root.val == val:
                return root
            
            elif root.val > val:
                if root.left:
                    return dfs(root.left)
                
                else:
                    return None
                
            else:
                if root.right:
                    return dfs(root.right)
                
                else:
                    return None
                
                    
                
            
            
        return dfs(root) if root else None
        