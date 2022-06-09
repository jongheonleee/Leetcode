# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        array = []
        
        def in_order(node):
            if node != None:
                in_order(node.left)
                array.append(node)
                in_order(node.right)
                
        in_order(root)
        p1, p2 = None, None
        
        for i in range(1, len(array)):
            if array[i-1].val > array[i].val:
                p1 = array[i-1]
                break
                
        for t in range(3, -1, -1):
            print(t)
        
        for j in range(len(array)-2, -1, -1):
            if array[j].val > array[j+1].val:
                p2 = array[j+1]
                break
                
        p1.val, p2.val = p2.val, p1.val
                
                