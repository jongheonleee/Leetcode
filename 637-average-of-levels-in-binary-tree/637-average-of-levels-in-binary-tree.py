# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        
        queue = collections.deque([root])
        
        while queue:
            sn, n = 0, 0
            for _ in range(len(queue)):
                node = queue.popleft()
                
                sn += node.val
                n += 1
                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                    
            ans.append(float(sn/n))
            
        return ans
