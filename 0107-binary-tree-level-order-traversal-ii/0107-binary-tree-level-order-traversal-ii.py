# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom1(self, root: Optional[TreeNode]) -> List[List[int]]:
        # this is my idea
        if root is None:
            return []
        
        # using bfs
        queue: Deque = collections.deque()
        queue.append(root)
        res = []
        
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
                
            res.append(tmp)
            
        return res[::-1]
    
    def levelOrderBottom2(self, root: Optional[TreeNode]) -> List[List[int]]:
        # using dfs
        res = []
        self.dfs(root, 0, res)
        return res
    
    def dfs(self, root:Optional[TreeNode], level: int, res: list) -> None:
        if root:
            if len(res) < level + 1:
                res.insert(0, [])
                
            res[-(level+1)].append(root.val)
            self.dfs(root.left, level+1, res)
            self.dfs(root.right, level+1, res)
            
        return None
    
    def levelOrderBottom3(self, root: Optional[TreeNode]) -> List[List[int]]:
        # using dfs by stack
        # tuple => (node, level)
        stack, res = [(root, 0)], []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level + 1:
                    res.insert(0, [])

                res[-(level+1)].append(node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))
            
        return res
    
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue:Deque = collections.deque([(root, 0)])
        res = []
        
        while queue:
            node, level = queue.popleft()
            if node:
                if len(res) < level+1:
                    res.insert(0, [])
                    
                res[-(level+1)].append(node.val)
                queue.append([node.left, level+1])
                queue.append([node.right, level+1])

        return res            
        
        
        
        