# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum1(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
        dfs recursively
        '''
        
        res = []
        def dfs(root, t):
            if root:
                if not root.left and not root.right and root.val == t:
                    res.append(True)
                    
                if root.left:
                    dfs(root.left, t-root.val)
                    
                if root.right:
                    dfs(root.right, t-root.val)
        
        dfs(root, targetSum)
        return any(res)
    
    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
        dfs stack
        '''
        
        if not root:
            return False
        
        st = [(root, root.val)]
        
        while st:
            crnt, val = st.pop()
            
            if not crnt.left and not crnt.right and val == targetSum:
                return True
            
            if crnt.right:
                st.append((crnt.right, val+crnt.right.val))
                
            if crnt.left:
                st.append((crnt.left, val+crnt.left.val))
                
        return False
    
    def hasPathSum3(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        q = [(root, targetSum-root.val)]
        while q:
            crnt, val = q.pop(0)
            
            if not crnt.left and not crnt.right and val == 0:
                return True
            
            if crnt.left:
                q.append((crnt.left, val-crnt.left.val))
                
            if crnt.right:
                q.append((crnt.right, val-crnt.right.val))
                
        return False
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right and root.val == targetSum:
            return True
        
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
    
    
                    
            
            
        