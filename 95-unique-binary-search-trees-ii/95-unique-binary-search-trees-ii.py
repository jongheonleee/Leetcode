# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        return self.helper(1, n)
    
    def helper(self, start, end):
        if start > end:
            return [None]
        
        all_trees = []
        
        for crnt_root_val in range(start, end+1):
            all_left_subtrees = self.helper(start, crnt_root_val-1)
            
            all_right_subtrees = self.helper(crnt_root_val+1, end)
            
            for left_subtree in all_left_subtrees:
                for right_subtree in all_right_subtrees:
                    crnt_root = TreeNode(crnt_root_val)
                    
                    crnt_root.left = left_subtree
                    crnt_root.right = right_subtree
                    
                    all_trees.append(crnt_root)
                    
        return all_trees
        
        

                    
                    
                
                    
                
                
            
                
                
            
        