# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """    
        def dfs(n1, n2):
            if not n1 and not n2:
                return True
            
            elif not n1 or not n2:
                return False
            
            
            elif n1.val !=  n2.val:
                return False
            
            return dfs(n1.left, n2.left) and dfs(n1.right, n2.right)
        
        return dfs(p, q)
                
        

        

                

                
                