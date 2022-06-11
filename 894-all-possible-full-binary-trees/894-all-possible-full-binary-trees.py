# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def clone(self, tree: TreeNode) -> TreeNode:
        # connected the (sub)tree on new_tree  
        if not tree:
            return None
        new_tree = TreeNode(0)
        new_tree.left = self.clone(tree.left)
        new_tree.right = self.clone(tree.right)
    
        return new_tree
  
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        # exception handling
        # it's possible make FBT when N is odd!! 
        if N % 2 == 0:
            return []
        
        elif N == 1:
            return [TreeNode(0)]
        
        ret = []
        # is's easier to imagine the nodes have a actual val from 1 to N
        # => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        # especially tree's root node & sub tree's root node have to be even number 
        # => [2, 4, 6, 8, 10]
        for i in range(2, N + 1, 2):
            left_branch = self.allPossibleFBT(i - 1)
            right_branch = self.allPossibleFBT(N - i)
            for left_count, left in enumerate(left_branch, 1):
                # 1: for default val on idx
                for right_count, right in enumerate(right_branch, 1):
                    tree = TreeNode(0)
          
                    # If we're using the last right branch, then this will be the last time this left branch is used and can hence
                    # be shallow copied, otherwise the tree will have to be cloned
                    tree.left = self.clone(left) if right_count < len(right_branch) else left
          
                    # If we're using the last left branch, then this will be the last time this right branch is used and can hence
                    # be shallow copied, otherwise the tree will have to be cloned
                    tree.right = self.clone(right) if left_count < len(left_branch) else right
          
                    ret.append(tree)
        return ret
    
    
            
                
            
            