# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
    
        def dfs(root, sum, ls):
            if root:
                if root.left == None and root.right == None and sum == targetSum:
                    res.append(ls)
                    return
                print(ls)
                if root.left:
                    dfs(root.left, sum+root.left.val, ls + [root.left.val])

                if root.right:
                    dfs(root.right, sum+root.right.val, ls + [root.right.val])
                
        if root:
            dfs(root, root.val, [root.val])
            
        return res
        
        
        