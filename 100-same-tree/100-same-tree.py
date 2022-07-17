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
        from collections import deque
        def check(p, q):
            if not p and not q:
                return True
            
            elif not p or not q:
                return False
            
            elif p.val != q.val:
                return False
            
            return True
            
        
        deq = deque([(p, q)])
        
        while deq:
            p, q = deq.popleft()
            
            if not check(p, q):
                return False
            
            if p and q:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
                
                
        return True
                
                
        

        

                

                
                