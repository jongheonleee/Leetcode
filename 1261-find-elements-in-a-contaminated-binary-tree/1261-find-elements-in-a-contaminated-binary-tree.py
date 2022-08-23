# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.seen = set()
        self.recover(self.root, self.seen)

    def recover(self, root, seen):
        queue = collections.deque([(root, 0)])
        
        while queue:
            node, val = queue.popleft()
            
            node.val = val
            seen.add(node.val)
            
            if node.left:
                queue.append((node.left, 2*val+1))
                
            if node.right:
                queue.append((node.right, 2*val+2))
                
       

    def find(self, target: int) -> bool:
        if target in self.seen:
            return True
        
        return False
  
            
                
                
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)