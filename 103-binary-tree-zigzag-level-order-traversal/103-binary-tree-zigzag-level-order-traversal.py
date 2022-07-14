# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder_(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 1. approach > bfs
        if root is None:
            return []
        
        res, direction = [], 1
        
        q = collections.deque([root])
        
        while q:
            level = []
            
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
            res.append(level[::direction])
            direction *= (-1)
            
        return res
    
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 2. approach > dfs(recursive)
        ans = []
        self.add_level(ans, 0, root)
        return ans
        
    
    
    
    
    
    def add_level(self, ans: list[list], level:int, root: Optional[TreeNode]):
        if not root:
            return 
        
        elif len(ans) <= level:
            ans.append([root.val])
            
        elif not level % 2:
            # when level is even
            # level ans should be original
            # so that i used extend()
            ans[level].extend([root.val])

        else:
            # when level is odd
            # level ans should be inversed
            # so that i used insert(0, val)
            ans[level].insert(0, root.val)
            
        self.add_level(ans, level+1, root.left)
        self.add_level(ans, level+1, root.right)
        
        
            