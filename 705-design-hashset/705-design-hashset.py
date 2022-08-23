class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        
        
class MyHashSet:

    def __init__(self):
        self.head = Node()
        self.set = set()
        self.crnt_node = self.head
        

    def add(self, key: int) -> None:
        if key in self.set:
            return 
        
        self.crnt_node.next = Node(key)
        self.crnt_node = self.crnt_node.next
        self.set.add(key)
        

    def remove(self, key: int) -> None:
        p1, p2 = self.head, self.head.next
        
        if key not in self.set:
            return 
        
        self.set.discard(key)
        
        while p2:
            if p1.val == key:
                p1.next = None
                return 
            
            if p2.val == key:
                p1.next = p2.next
                p2.next = None
                return
            
            p1 = p1.next
            p2 = p2.next

                
        

    def contains(self, key: int) -> bool:
        if key in self.set:
            return True
        
        return False
    
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)