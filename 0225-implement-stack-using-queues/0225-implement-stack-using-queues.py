class MyStack:

    def __init__(self):
        self.queue:list = []
            
    def move(self):
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.pop(0))
            
        
    def push(self, x: int) -> None:
        self.queue.append(x)
        
    def pop(self) -> int:
        self.move()
        return self.queue.pop(0)
        
        
    def top(self) -> int:
        self.move()
        item = self.queue.pop(0)
        self.queue.append(item)
        
        return item
        
    def empty(self) -> bool:
        return True if len(self.queue) == 0 else False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()