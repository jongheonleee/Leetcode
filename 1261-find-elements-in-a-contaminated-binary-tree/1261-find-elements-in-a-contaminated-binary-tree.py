# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.recover(self.root)

    def recover(self, root):
        queue = collections.deque([(root, 0)])
        
        while queue:
            node, val = queue.popleft()
            
            node.val = val

            
            if node.left:
                queue.append((node.left, 2*val+1))
                
            if node.right:
                queue.append((node.right, 2*val+2))
                
       

    def find(self, target: int) -> bool:
        queue = collections.deque([self.root])
        
        while queue:
            node = queue.popleft()
            
            if node.val == target:
                return True
            
            if node.val < target:
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                    
            else:
                return False
  
            
                
                
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)